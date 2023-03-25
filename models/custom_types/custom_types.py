from sqlalchemy.types import TypeDecorator, Numeric

class CustomNumeric(TypeDecorator):
    impl = Numeric
    
    def process_result_value(self, value, dialect):
        return float(value) if value is not None else None