#!/usr/bin/env python3
import argparse

def compute(cp: float, sp: float):
    profit = sp - cp
    margin = (profit / sp * 100) if sp else 0
    markup = (profit / cp * 100) if cp else 0
    return profit, margin, markup

def main():
    p = argparse.ArgumentParser(description="Margin Calculator")
    p.add_argument("--cp", type=float, required=True, help="Cost Price")
    p.add_argument("--sp", type=float, required=True, help="Selling Price")
    args = p.parse_args()
    profit, margin, markup = compute(args.cp, args.sp)
    print(f"Cost Price: {args.cp:.2f}")
    print(f"Selling Price: {args.sp:.2f}")
    print(f"Profit: {profit:.2f}")
    print(f"Margin: {margin:.2f}%")
    print(f"Markup: {markup:.2f}%")

if __name__ == "__main__":
    main()