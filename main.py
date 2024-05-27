import datetime, bday_messages as bd

today = datetime.date.today()

next_birthday = datetime.date(2025,5,6)

days_away = (next_birthday - today).days

print(f"{bd.random_message}") if today == next_birthday else print(f'Faltam {days_away} dias para o seu aniversário!')