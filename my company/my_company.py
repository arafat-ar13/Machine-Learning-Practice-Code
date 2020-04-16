import calendar
import smtplib
import os
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from time import sleep, strftime

print("Hello. Welcome to our company. We provide hotel, rental car and flights services for people in the US. Please go ahead and make your selections")
sleep(1.5)

now = datetime.now()

user_hotel_nights = int(input("How many nights you want in? "))

user_hotel_cost = 0


def hotel_picker(user_selected_nights):
    cost_per_night = 220
    global user_hotel_cost
    user_hotel_cost = cost_per_night * user_selected_nights
    return(f"Your total cost for staying {user_selected_nights} nights at our place will be ${user_hotel_cost}")


sleep(0.5)
print(hotel_picker(user_hotel_nights))

cities_available = {
    "los angeles": 123,
    "atlanta": 150,
    "miami": 172,
    "chicago": 135,
    "new york city": 200,
    "philadelphia": 231,
    "reading": 199,
    "nashville": 212,
    "springfield": 230,
    "college park": 173,
    "manhattan": 213,
    "cincinnati": 210,
    "phoenix": 176,
    "atlantic city": 155
}


cities_available_list = []

for city in cities_available:
    cities_available_list.append(city)


glorious_city_manager = ', '. join(cities_available_list[:len(
    cities_available) - 1]).title() + ' and ' + cities_available_list[-1].title()
sleep(2)
print(f"We allow flights to {glorious_city_manager} for now")
sleep(1.5)

user_flight_to = input("Where do you wanna be flying to? ").lower()


while user_flight_to not in cities_available:
    user_flight_to = input(
        "You must've mistyped the city name. Please take a look again and try again. ")

if user_flight_to in cities_available:
    user_city_cost = cities_available[user_flight_to]
    sleep(1.23)
    print(
        f"For flying to {user_flight_to.title()} your cost will be ${user_city_cost}")


sleep(2)
print("We also have car rental services to provide our customers with")
sleep(2)
print("We have partenered with Uber to provide the best traveling experience for our customers")
sleep(2.5)

user_car_choice = input(
    "So, do you want to use our car rental services? ").lower()

user_car_cost = 0
user_car_days = 0
if user_car_choice == "yes":
    sleep(1.69)
    car_days_same_as_hotel_days = input(
        "Do you want to use the car for the same number of days as you'll be staying in our hotel? ").lower()
    if car_days_same_as_hotel_days == "yes" or car_days_same_as_hotel_days == "yeah":
        user_car_days = user_hotel_nights
    else:
        sleep(1.693)
        user_car_days = int(
            input("For how many days do you want to user our car? "))

    def user_car(days):
        price_per_day_of_using_car = 45
        global user_car_cost
        user_car_cost = price_per_day_of_using_car * days
        return(f"For using the car for {days} days, your cost will be ${int(user_car_cost)}")
    sleep(2)
    print(user_car(user_car_days))
else:
    sleep(1)
    print("Okay then, have a nice day finding a car")


def user_total_cost():
    global user_total
    user_total = user_hotel_cost + user_city_cost + user_car_cost
    return(f"Your total cost would be ${user_total}")


print(user_total_cost())


user_final_choice = input(
    "So, do you want to purchase your options and choice? ")


if user_final_choice == "yes":
    user_name = input("Please enter your name, Sir: ")
    user_email_address = input("Please enter your email address: ")

    def sendMail():
        ampm = "PM" if now.hour > 12 else "AM"
        if user_car_days == 0:
            user_car_string = "Lastly, you didn't choose to use our car services."
            user_intro_string = f"Around {strftime('%I:%M')} {ampm} on {now.month}/{now.day}/{now.year} you bought Hotel and Flight services from my company"
        elif user_car_days > 0:
            user_intro_string = f"Around {strftime('%I:%M')} {ampm} on {now.month}/{now.day}/{now.year} you bought Hotel, Flight and Car Rental services from my company"
            user_car_string = f"Lastly, you'll be willing to use our car rental services for {user_car_days} days, costing you ${user_car_cost}."
        try:
            my_email = os.environ.get("GOOGLE_ACCOUNT")
            my_password = os.environ.get("GOOGLE_ACCOUNT_PASS")

            send_to_email = user_email_address
            subject = "Thanks for shopping at our place"
            message_body = f"""Dear, {user_name}
                        <br>
                        {user_intro_string}. 
                        <br>
                        You're flying to {user_flight_to.title()} and that's gonna set you ${user_city_cost}.
                        <br>
                        You're staying {user_hotel_nights} nights at our hotel, for that you're paying ${user_hotel_cost}. 
                        <br>
                        {user_car_string} 
                        <br>
                        Your total cost for shopping at our place was: ${user_total}.
                        """

            msg = MIMEMultipart()
            msg["From"] = my_email
            msg["To"] = send_to_email
            msg["Subject"] = subject

            msg.attach(MIMEText(message_body, "html"))

            server = smtplib.SMTP(host="smtp.gmail.com", port=587)
            server.starttls()
            server.login(my_email, my_password)

            text_as_string = msg.as_string()

            server.sendmail(my_email, send_to_email, text_as_string)
            server.quit()

            return("Message sent successfully")

        except:
            return("Oops! Couldn't send the email")

    print(sendMail())