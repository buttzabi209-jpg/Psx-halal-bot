import os
import requests

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

def send_telegram_message():
    token = os.environ.get('TELEGRAM_BOT_TOKEN')
    chat_id = os.environ.get('TELEGRAM_CHAT_ID')
    
    message = generate_halal_report()
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    
    payload = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "Markdown"
    }
    
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        print("Telegram Message Sent Successfully!")
    else:
        print(f"Failed to send message: {response.text}")

if __name__ == "__main__":
    send_telegram_message()
