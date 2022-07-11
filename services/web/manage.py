from flask.cli import FlaskGroup

from project import app, db, InputData


cli = FlaskGroup(app)


@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command("seed_db")
def seed_db():
    input_data = [

        {"date": "12/01/2020", "slot_id": 123, "device": "desktop", "impressions": 3000},
        {"date": "12/01/2020", "slot_id": 123, "device": "mobile", "impressions": 2000},
        {"date": "12/01/2020", "slot_id": 123, "device": "tablet", "impressions": 1000},
        {"date": "12/02/2020", "slot_id": 123, "device": "desktop", "impressions": 2500},
        {"date": "12/02/2020", "slot_id": 123, "device": "mobile", "impressions": 1500},
        {"date": "12/02/2020", "slot_id": 123, "device": "tablet", "impressions": 500},
        {"date": "12/03/2020", "slot_id": 123, "device": "desktop", "impressions": 500},
        {"date": "12/03/2020", "slot_id": 123, "device": "mobile", "impressions": 500},
        {"date": "12/03/2020", "slot_id": 123, "device": "tablet", "impressions": 100}
    ]
    for data in input_data:
        db.session.add(InputData(slot_id=data["slot_id"],
                                 date=data["date"],
                                 device=data["device"],
                                 impressions=data["impressions"]
                                  ))
        db.session.commit()


if __name__ == "__main__":
    cli()