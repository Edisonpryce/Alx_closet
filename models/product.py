class Product:
    __tablename__ = 'product'
    name = Column(String(40), nullable=False)
    description = Column(String(128), nullable=False)
    category = Column(String(128), nullable=True)
    price = Column(decimal(10), nullable=True)