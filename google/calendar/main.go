package main

import (
	"context"
	"errors"
	"fmt"
	"github.com/obot-platform/tools/google/calendar/pkg/commands"
	"golang.org/x/oauth2"
	"google.golang.org/api/calendar/v3"
	"google.golang.org/api/option"
	"log"
	"os"
	"time"
)

func getClient(ctx context.Context) (*calendar.Service, error) {
	accessToken := os.Getenv("GOOGLE_OAUTH_TOKEN")
	if accessToken == "" {
		return nil, errors.New("Please set GOOGLE_OAUTH_TOKEN env var")
	}
	tok := &oauth2.Token{AccessToken: accessToken}
	src := oauth2.StaticTokenSource(tok)
	httpClient := oauth2.NewClient(ctx, src)
	srv, err := calendar.NewService(ctx, option.WithHTTPClient(httpClient))
	if err != nil {
		return nil, err
	}
	return srv, nil
}

func main() {
	var err error
	if len(os.Args) != 2 {
		log.Fatalln("Usage: gcal <command>")
	}
	command := os.Args[1]

	ctx := context.Background()
	client, err := getClient(ctx)
	if err != nil {
		log.Fatal(err)
	}

	switch command {
	// Issues
	case "searchCalendar":
		query := os.Getenv("SEARCH_QUERY")
		calendarID, exists := os.LookupEnv("CALENDAR_ID")
		if !exists {
			calendarID = "primary"
		}
		timeZone, exists := os.LookupEnv("OBOT_USER_TIMEZONE")
		if !exists {
			timeZone = "UTC"
		}
		location, err := time.LoadLocation(timeZone)
		if err != nil {
			break
		}
		now := time.Now().In(location)
		timeMin, exists := os.LookupEnv("START_TIME_RANGE")
		if !exists {
			timeMin = time.Date(now.Year(), now.Month(), now.Day(), 0, 0, 0, 0, location).Format(time.RFC3339)
		}
		timeMax, exists := os.LookupEnv("END_TIME_RANGE")
		if !exists {
			timeMax = time.Date(now.Year(), now.Month(), now.Day(), 23, 59, 59, 0, location).Format(time.RFC3339)
		}

		fmt.Println("case search calendar")
		fmt.Printf("search query: %s\n", query)
		fmt.Printf("search time range: '%s'-'%s\n", timeMin, timeMax)
		fmt.Printf("time zone: '%s'\n", timeZone)
		err = commands.SearchCalendar(client, calendarID, timeMin, timeMax, timeZone, query)
	default:
		err = errors.New(fmt.Sprintf("Unknown command: %s\n", command))
	}

	if err != nil {
		log.Fatal(err)
	}
}
