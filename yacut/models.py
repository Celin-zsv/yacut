from datetime import datetime

from flask import url_for

from yacut import db
from .constants import MODEL_FIELD_TO_JSON_FIELD


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(256), nullable=False)
    short = db.Column(db.String(16), unique=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def from_dict(self, data):
        for model_field, json_field in MODEL_FIELD_TO_JSON_FIELD.items():
            if json_field in data:
                setattr(self, model_field, data[json_field])

    def to_dict(self):
        return dict(
            url=self.original,
            short_link=url_for('index_view', _external=True) + self.short
        )
