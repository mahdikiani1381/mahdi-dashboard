import streamlit as st
from crypto_price import get_dollar_price, get_bitcoin_price
from recommender import get_investment_advice
from analysis import get_market_status, get_weekly_report

st.set_page_config(page_title="داشبورد سرمایه‌گذاری مهدی", layout="centered")

st.title("📊 داشبورد سرمایه‌گذاری مهدی")

# نمایش وضعیت بازار
status = get_market_status()
st.subheader("🔍 وضعیت بازار:")
st.info(status)

# قیمت ارز و رمز ارز
dollar = get_dollar_price()
bitcoin = get_bitcoin_price()
st.subheader("💰 قیمت‌ها:")
st.write(f"💵 دلار: {dollar} تومان")
st.write(f"₿ بیت‌کوین: {bitcoin} دلار")

# پیشنهاد سرمایه‌گذاری
advice = get_investment_advice()
st.subheader("📈 پیشنهاد سرمایه‌گذاری:")
st.success(advice)

# گزارش هفتگی
report = get_weekly_report()
st.subheader("🗓 گزارش هفتگی:")
st.code(report, language='markdown')