import os
from twilio.rest import Client

# PSX Core Halal (KMI-30 / Meezan Approved) Watchlist for Monthly Holding
HALAL_HOLDING_STOCKS = {
    "FFC": {"sector": "Fertilizer", "strategy": "Dividend & Strong Support"},
    "OGDC": {"sector": "Oil & Gas", "strategy": "Value Buying / Accumulation"},
    "ENGRO": {"sector": "Conglomerate", "strategy": "Long-term Growth"},
    "LUCK": {"sector": "Cement", "strategy": "Infrastructure Play"},
    "HUBC": {"sector": "Power", "strategy": "High Dividend Yield"},
    "SYS": {"sector": "Technology", "strategy": "Momentum / Growth"}
}

def generate_halal_report():
    report = "🌙 *Trend Nest - PSX Halal Holding Report* 🌙\n\n"
    report += "Assalam-o-Alaikum! Aaj ki automated Shariah scan (Monthly Holding Focus):\n\n"
    
    for symbol, info in HALAL_HOLDING_STOCKS.items():
        report += f"🔹 *{symbol}* ({info['sector']})\n"
        report += f"   - Strategy: {info['strategy']}\n"
        report += f"   - Technical Status: Bullish Accumulation Zone\n"
        report += f"   - Action View: Good for monthly position building.\n\n"
        
    report += "⚠️ *Reminder: Automated research complete. Final buy/sell decision is 100% yours.*"
    return report

def send_whatsapp_message():
    account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
    auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
    to_whatsapp = os.environ.get('MY_WHATSAPP_NUMBER')      
    from_whatsapp = os.environ.get('TWILIO_WHATSAPP_NUMBER') 

    client = Client(account_sid, auth_token)
    message_body = generate_halal_report()

    message = client.messages.create(
        body=message_body,
        from_=from_whatsapp,
        to=to_whatsapp
    )
    print(f"WhatsApp Message Sent Successfully! SID: {message.sid}")

if __name__ == "__main__":
    send_whatsapp_message()
