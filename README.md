# <p align="center">[The Relevant Devpost](https://devpost.com/software/city-of-dallas-division-of-crime-and-public-safety) </p>

# HackSMU_22
Superhero Dispatch Startup for HackSMU 22, contains code for everything we did.

<img src="assets/images/dallas_city_logo.png"></img>

## Members
- Sam Yao
- Cait Prough
- Joey Luu
- Sebastian Rodriguez

## Inspiration
As we were brainstorming ideas for what our project should be, we jokingly had said to create either a superhuman agency startup, or an alerting system that would warn you when you were being robbed or if you were being chased by the police (basically alerts for criminals). Eventually, we actually made both of these ideas a reality though, with some tweaks obviously, and were able to combine multiple of our skill sets into the project by combining these ideas, too.

## What it does
Using Twilio, we were able to program alerts, being sent from a virtual phone number given to us by Twilio, and sent to Sebastian and Cait's phones. What the Twilio program does is send Sebastian and Cait an alert about any current accidents in DFW; The way we did this was by pulling data from a webpage, that has data regarding incident reports, and using that data in the programmable message that we made. Also, we created a website where we have our fictitious organization's main page on, where we mimicked what we thought a public safety branch website would look like. The website is pretty basic, but we wanted to have a place where we would have integrated the Twilio program, for people to sign up for those alerts, as well as have a user interface where residents could be informed about current incidents in the area, and find out more about the actual department.

## How we built it
For the SMS alerts, we utilized the tools that Twilio provides on their website, and quick-start guides in order to create a basic program that would send code to us. Then, a program sends crime alerts to the phones of people that signed up. We also built a website for our organization, the City of Dallas Department of Crime and Public Safety (which does not actually exist)

## Challenges we ran into
Currently, GitHub Pages is not wanting to work with us right now, so we were not able to link our page with the custom domain that we made with Domain.com. Some other issues that we ran into was figuring out why our Twilio code wasn't compiling at one point, and finding where the bug or issue was. Also, we spent a long time just trying to come up with an idea on what to implement, and how to utilize Twilio's software. Lastly, getting the data from the database that we planned on using was a challenge, especially when the database completely shut down temporarily, meaning we couldn't pull data from there either.

## Accomplishments that we're proud of
We were able to send texts from Twilio's virtual phone to our actual phones, and eventually, we were also able to send messages with updated data that we pulled from the DFW database (and it wouldn't send an incident more than once if no new ones appeared, which we were especially proud of implementing). Also, being able to finally see that the data from the DFW incident report database was actually being pulled, was very awesome to see! Lastly, we were really proud to see how our website turned out, considering we all had little to no experience in web development.

## What we learned
One major thing that we learned how to use Twilio's software to make programmable messages to send to our phone numbers. We also learned how to use Google Colaboratory to pull the data from the Dallas incident report database, which we then learned how to integrate into the Twilio code to send alerts with that data that we pulled.

## What's next for City of Dallas Division of Crime and Public Safety
Some major updates that we wanted to implement, but didn't have the time to implement during the hackathon, was integrating the Twilio API into the website, so that people, especially superheroes, could be alerted of the current incident reports. Also, we wanted to program our Twilio software to not only send messages, but also receive them. Lastly, we truly wanted to add more to our website so that the website would be very user-friendly and easy to navigate, and actually get involved with the city of Dallas (in a perfect world where superheroes actually exist)!