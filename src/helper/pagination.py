from src.model.base_model import CustProfile


class Pagination:
    count = CustProfile.select().count()
    record_per_page = 500
    page = int(count / record_per_page)

