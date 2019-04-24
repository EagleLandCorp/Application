import app.calendar as calendar

def test1():
    # User ID 1
    user1id = "auth0|5cb50516ee4bd5113d54872b"    # Jareds ID!

    # User ID 2
    user2id = "auth0|5cbe466fd1f05811d6866c0b"    # Jacobs ID!

    # Range
    start = "2019-04-01T00:00:00-04:00" # year-month-day(T)two digit hours: two digit minutes: two digit seconds(-04 is subtracted from UTC, this for example is EST eastern time)
    end = "2019-04-02T00:00:00-04:00"
    timezone = "America/New_York" #only use this as the timezone

  #  calendar1 = calendar.get_calendar(user1id, start, end, timezone)
   # calendar2 = calendar.get_calendar(user2id, start, end, timezone)


    # Correct return value
    freeevents = [
        calendar.Event("2019-04-15T11:50:00-04:00", "2019-04-15T12:00:00-04:00")
        # Create a calendar containing the correct shared freetimes between both user calendars.
    ]
    freecalendar = calendar.Calendar(freeevents)

    result = calendar.compare_user_calendars(user1id, user2id, start, end, timezone)
    assert result == freecalendar


if __name__ == '__main__':
    test1()
    print("Passed all tests.")
