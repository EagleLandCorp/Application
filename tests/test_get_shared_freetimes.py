import app.calendar as calendar


def test1():
    # Example calendar 1
    user1events = [
        calendar.Event("2019-04-15T11:00:00-04:00", "2019-04-15T11:50:00-04:00")
    ]
    calendar1 = calendar.Calendar(user1events)

    # Example calendar 2
    user2events = [
        calendar.Event("2019-04-15T12:00:00-04:00", "2019-04-15T12:50:00-04:00")
    ]
    calendar2 = calendar.Calendar(user2events)

    # Correct return value
    freeevents = [
        calendar.Event("2019-04-15T11:50:00-04:00", "2019-04-15T12:00:00-04:00")
    ]
    freecalendar = calendar.Calendar(freeevents)

    rangestart = "2019-04-15T11:00:00-04:00"
    rangeend = "2019-04-15T12:50:00-04:00"
    result = calendar.get_shared_freetimes(rangestart, rangeend, calendar1, calendar2)
    result_string =""
    for event in result:
        result_string += event.starttime + ' - ' + event.endtime + '\n'
    print(result_string)
    assert result == freecalendar


if __name__ == '__main__':
    test1()
    print("Passed all tests.")