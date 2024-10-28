package main

import (
	"encoding/csv"
	"fmt"
	"log"
	"os"

	"github.com/gocolly/colly"
)

type Stock struct {
	company, price, change string
}

func main() {
	tickers := []string{
		"MSFT",
		"IBM",
		"GE",
		"UNP",
		"COST",
		"MCD",
		"V",
		"WMT",
		"DIS",
		"MMM",
		"INTC",
		"AXP",
		"AAPL",
		"BA",
		"CSCO",
		"GS",
		"JPM",
		"CRM",
		"VZ",
	}

	stocks := []Stock{}
	c := colly.NewCollector()

	c.OnRequest(func(r *colly.Request) {
		fmt.Println("Visiting:", r.URL)
	})

	c.OnError(func(_ *colly.Response, err error) {
		log.Println("Something went wrong:", err)
	})

	c.OnHTML("div#quote-header-info", func(e *colly.HTMLElement) {
		stock := Stock{}
		stock.company = e.ChildText("h1")
		stock.price = e.ChildText("fin-streamer[data-field='regularMarketPrice']")
		stock.change = e.ChildText("fin-streamer[data-field='regularMarketChangePercent']")

		// Print extracted values to verify
		fmt.Println("Company:", stock.company, "Price:", stock.price, "Change:", stock.change)

		if stock.company != "" && stock.price != "" && stock.change != "" {
			stocks = append(stocks, stock)
		} else {
			fmt.Println("Error: Could not extract data for this ticker")
		}
	})

	// Loop through each ticker and visit its URL
	for _, t := range tickers {
		url := "https://finance.yahoo.com/quote/" + t
		c.Visit(url)
	}

	// Wait for all requests to finish
	c.Wait()

	// Print all stocks collected
	fmt.Println(stocks)

	// Create the output CSV file
	file, err := os.Create("stocks.csv")
	if err != nil {
		log.Fatalln("Failed to create the output CSV file", err)
	}
	defer file.Close()

	writer := csv.NewWriter(file)
	defer writer.Flush() // Ensure data is written to file

	// Write headers
	headers := []string{"company", "price", "change"}
	if err := writer.Write(headers); err != nil {
		log.Fatalln("Failed to write headers to CSV", err)
	}

	// Write stock data to CSV
	for _, stock := range stocks {
		record := []string{stock.company, stock.price, stock.change}
		if err := writer.Write(record); err != nil {
			log.Fatalln("Failed to write record to CSV", err)
		}
	}

	fmt.Println("Stock data has been written to stocks.csv")
}
