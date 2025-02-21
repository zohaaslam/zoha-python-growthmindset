#streamlit 

import streamlit as st

st.set_page_config(page_title = "Growth Mindset Project ", page_icon= "★")
st.title("Growth Mindset Challenge: Web App with Streamlit")

st.header("🚀 Welcome to Your Growth journey!")
st.write("Embrace challenges, learn from mistakes, and unlock your full potential. This AI-powered app helps you build a growth mindset with reflection, challenges, and achievements!🌟 ")


#quote section

st.header("💡 Today's Growth Minset Quote")
st.write("“Sucess is not final, failure is not fatal: it is the courage to continue that counts.”- Winston Churchill")


#challenge section

st.header("🌱 What's Your Growth Challenge Today?")
user_input = st.text_input("Describe a challenge you're facing :")

#condition 

if user_input:
    st.sucees(f"💪You're fcing : {user_input}.Keep pushing forward towards your goal!🚀")

else:
    st.warning("Tell us about you're challenge to get started!🌟")


#reflecting section

st.header("🌟 Reflect on Your Learning")
reflection = st.text_area("Write your reflection here:")

if reflection:
    st.success(f"✨Great Insight! reflection: {reflection}")

else:
    st.info("Reflection on past experience help you grow! Share your difficulties")



 #achievments

st.header("🏆 Celebrate Your Wins!")
achievement = st.text_input("Share something you've recently accomplished:")


if achievement:
    st.success(f"🎉 Amazing! You've achieved: {achievement}")

else :
    st.info("Big or small, every acheivement counts! Share one now 😊🌟")


#footer 

st.write("- - - ")
st.write("Keep believing in yourself and remember that you have the power to grow and achieve anything you set your mind to!🌟")
st.write("***Created  by Zoha Aslam ❤️***")