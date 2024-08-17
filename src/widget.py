from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(number: str) -> str | None:
    if len(number.split()[-1]) == 16:
        new_number = get_mask_card_number(number.split()[-1])
        result = f"{number[:-16]}{new_number}"
        return result
    elif len(number.split()[-1]) == 20:
        new_number = get_mask_account(number.split()[-1])
        result = f"{number[: -20]}{new_number}"
        return result
    else:
        return None


def get_new_data(old_data: str) -> str:
    data_slize = old_data[0:10].split("-")
    return ".".join(data_slize[::-1])

from datetime import datetime
from src.masks import get_mask_account, get_mask_card_number

def mask_account_card(card_or_account_info: str) -> str:
    """принимает название и номер карты или номер счета и возвращает замаскированный номер"""
    payment_info = card_or_account_info.split(" ")
    payment_number = int(payment_info[-1])
    payment_name = payment_info[:-1]
    if card_or_account_info.lower().startswith("счет"):
        number = get_mask_account(payment_number)
    else:
        number = get_mask_card_number(payment_number)
    return " ".join(payment_name) + f" {number}"


def get_date(date_info: str) -> str:
    """преобразует дату в формат dd.mm.yy"""
    converted_date = datetime.fromisoformat(date_info).strftime("%d.%m.%Y")
    return converted_date


#if __name__ == "__main__":
#    print(mask_account_card("Maestro 1596837868705199"))
#    print(mask_account_card("Счет 64686473678894779589"))
#    print(mask_account_card("Visa Classic 6831982476737658"))
#    print(get_date("2018-07-11T02:26:18.671407"))