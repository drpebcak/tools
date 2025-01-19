package commands

import (
	"fmt"
	"google.golang.org/api/calendar/v3"
)

func SearchCalendar(client *calendar.Service, calendarID, timeMin, timeMax, timeZone, query string) error {
	fmt.Println("Calendar search")
	events, err := client.Events.List(calendarID).TimeMin(timeMin).TimeMax(timeMax).TimeZone(timeZone).Q(query).Do()
	if err != nil {
		fmt.Printf("Error searching events: %v\n", err)
		return err
	}
	fmt.Println("Events:")
	if len(events.Items) == 0 {
		fmt.Println("No events found")

	} else {
		for _, event := range events.Items {
			date := event.Start.DateTime
			if date == "" {
				date = event.Start.Date
			}
			fmt.Printf("%s %s %s\n", date, event.Summary, event.Id)
		}
	}
	return nil
}
