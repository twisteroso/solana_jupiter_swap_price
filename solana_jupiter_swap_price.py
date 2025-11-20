import requests

def jupiter_price(input_mint: str, output_mint: str, amount: int):
    url = f"https://quote-api.jup.ag/v6/quote?inputMint={input_mint}&outputMint={output_mint}&amount={amount}&slippageBps=50"
    data = requests.get(url).json()["data"][0]
    out = int(data["outAmount"]) / 10**int(data["outAmountDecimals"])
    price = out / (amount / 10**int(data["inAmountDecimals"]))
    print(f"1 {data['inTokenSymbol']} → {price:.10f} {data['outTokenSymbol']}\n"
          f"Маршрут: {' → '.join(t['symbol'] for t in data['marketInfos'][:3])}{' → ...' if len(data['marketInfos'])>3 else ''}")

if __name__ == "__main__":
    inp = input("From (SOL/USDC/etc): ").upper()
    out = input("To: ").upper()
    amt = float(input("Amount: "))
    mints = {"SOL":"So11111111111111111111111111111111111111112", "USDC":"EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v"}
    jupiter_price(mints.get(inp,inp), mints.get(out,out), int(amt * 1e9 if inp=="SOL" else amt*1e6))
