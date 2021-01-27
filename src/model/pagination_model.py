from src.model.base_model import CustProfile


class paginate_page:
    count_all_record = CustProfile.select().count()
    record_per_page = 500
    page_all = int(count_all_record / record_per_page)