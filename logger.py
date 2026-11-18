import datetime
import sqlite3


class Logger:
  _instance = None

  def __new__(cls):
    if cls._instance is None:
      cls._instance = super().__new__(cls)
      cls._instance._initialise()
    return cls._instance

  def _initialise(self):
    self.connexion = sqlite3.connect("logs.db")
    self.connexion.execute(
        "CREATE TABLE IF NOT EXISTS logs (ts TEXT, message TEXT)"
    )
    self.connexion.commit()

  def log(self, message: str) -> None:
    ts = datetime.datetime.now().isoformat()
    self.connexion.execute("INSERT INTO logs VALUES (?, ?)", (ts, message))
    self.connexion.commit()
    print(f"[{ts}] {message}")

  def tous_les_logs(self) -> list[tuple]:
    return self.connexion.execute("SELECT * FROM logs").fetchall()

  def fermer(self) -> None:
    if self.connexion:
      self.connexion.close()
