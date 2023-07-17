from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

Base = declarative_base()


class BacktestRun(Base):
    __tablename__ = "backtest_runs"
    id = Column(Integer, primary_key=True)

    run_id = Column(String)
    scheduled_time = Column(DateTime)
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    input = Column(String)
    output = Column(String)

    def __repr__(self):
        return (
            f"<BacktestRun("
            f"run_id='{self.run_id}', "
            f"scheduled_time='{self.scheduled_time}', "
            f"start_time='{self.start_time}', "
            f"end_time='{self.end_time}', "
            f"input='{self.input}', "
            f"output='{self.output}')>"
        )
