from datetime import datetime,timedelta

def data():
    user_data={}
    user_data['name'] = input("Enter your name:")
    user_data['card'] = float(input("Enter the card balance:"))
    user_data['wallet'] = float(input("Enter the cash in your wallet :"))
    user_data['meals'] = float(input("Enter the spend one meals using your wallet money:"))
    user_data['travel'] = float(input("Enter the spend for travel:"))
    user_data['No_of_days'] = int(input("Enter the number of days go to the office:"))
    user_data['start_date'] = input("Enter the start date indd/mm/yyyy format:")
    return user_data

def calculate_travel_cost(user_data):
    daily_travel_cost = user_data['travel']*2  
    daily_meals_cost = user_data['meals']
    total_travel_cost = daily_travel_cost*user_data['No_of_days']      
    total_meal_cost = daily_meals_cost * user_data['No_of_days']
    return total_travel_cost, total_meal_cost

def check_balance(user_data, total_travel_cost, total_meal_cost):
    enough_card_balance = user_data['card'] >= total_travel_cost
    enough_wallet_balance = user_data['wallet'] >= total_meal_cost
    return enough_card_balance, enough_wallet_balance

def calculate_end_date(start_date_str, no_of_days):
    start_date = datetime.strptime(start_date_str, "%d/%m/%Y")
    end_date = start_date + timedelta(days=no_of_days)
    return end_date.strftime("%d/%m/%Y")

def main():
    user_data = data()
    total_travel_cost, total_meal_cost = calculate_travel_cost(user_data)
    enough_card_balance, enough_wallet_balance = check_balance(user_data, total_travel_cost, total_meal_cost)
    end_date = calculate_end_date(user_data['start_date'], user_data['No_of_days'])

    print(f"\nName: {user_data['name']}")
    print(f"Total travel cost for {user_data['No_of_days']} days: {total_travel_cost:.2f}")
    print(f"Total meal cost for {user_data['No_of_days']} days: {total_meal_cost:.2f}")

    if enough_card_balance and enough_wallet_balance:
        print("You have enough balance in both your card and wallet.")
    else:
        print("You do not have enough balance.")
        if not enough_card_balance:
            print("Your card balance is insufficient.")
        if not enough_wallet_balance:
            
            print("Your wallet balance is insufficient.")

    print(f"End date after {user_data['No_of_days']} days from start date {user_data['start_date']} is: {end_date}")

if __name__ == "__main__":
    main()

