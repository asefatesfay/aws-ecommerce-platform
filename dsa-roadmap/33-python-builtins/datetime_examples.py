"""
datetime — Date and time manipulation.

Covered here:
  date          — year, month, day; arithmetic, formatting, parsing
  time          — hour, minute, second, microsecond, tzinfo
  datetime      — combined date + time; arithmetic with timedelta
  timedelta     — duration; add/subtract from date/datetime
  timezone      — UTC and fixed-offset timezones
  strftime      — format datetime to string
  strptime      — parse string to datetime
  date arithmetic — business days, age, countdown, scheduling
  zoneinfo      — IANA timezone database (Python 3.9+)
  Practical patterns — ISO 8601, Unix timestamps, age calculation,
                       relative time ("2 hours ago"), schedule generation
"""

from datetime import date, time, datetime, timedelta, timezone, MINYEAR, MAXYEAR
import time as time_module


# ---------------------------------------------------------------------------
# 1. date basics
# ---------------------------------------------------------------------------

def demo_date():
    print("=" * 60)
    print("date")
    print("=" * 60)

    today = date.today()
    print("today():         ", today)
    print("year:            ", today.year)
    print("month:           ", today.month)
    print("day:             ", today.day)
    print("isoformat():     ", today.isoformat())         # '2026-04-10'
    print("strftime:        ", today.strftime("%B %d, %Y"))  # 'April 10, 2026'
    print("weekday():       ", today.weekday())           # 0=Mon … 6=Sun
    print("isoweekday():    ", today.isoweekday())        # 1=Mon … 7=Sun
    print("isocalendar():   ", today.isocalendar())       # (year, week, weekday)

    # Construction
    birthday  = date(1990, 7, 4)
    from_ord  = date.fromordinal(738_000)
    print("\ndate(1990,7,4):", birthday)
    print("fromordinal:  ", from_ord)

    # Parsing from ISO string
    d = date.fromisoformat("2026-12-25")
    print("fromisoformat:", d)

    # Arithmetic
    later = today + timedelta(days=90)
    print(f"\n90 days from today: {later}")

    delta = d - today
    print(f"Days until {d}: {delta.days}")

    # Min / max
    print(f"\ndate.min: {date.min}  date.max: {date.max}")

    print()


# ---------------------------------------------------------------------------
# 2. time basics
# ---------------------------------------------------------------------------

def demo_time():
    print("=" * 60)
    print("time")
    print("=" * 60)

    t = time(14, 30, 45, 123456)
    print("time(14,30,45,us):", t)
    print("hour:   ", t.hour)
    print("minute: ", t.minute)
    print("second: ", t.second)
    print("microsecond:", t.microsecond)
    print("isoformat(): ", t.isoformat())     # '14:30:45.123456'
    print("strftime: ", t.strftime("%I:%M %p"))  # '02:30 PM'

    # time with timezone
    utc = timezone.utc
    t_utc = time(12, 0, 0, tzinfo=utc)
    print("\ntime with UTC:", t_utc)

    # Fixed offset timezone (+5:30 for IST)
    ist = timezone(timedelta(hours=5, minutes=30))
    t_ist = time(17, 30, 0, tzinfo=ist)
    print("time with IST:", t_ist)

    print()


# ---------------------------------------------------------------------------
# 3. datetime basics — the workhorse class
# ---------------------------------------------------------------------------

def demo_datetime_basics():
    print("=" * 60)
    print("datetime — combined date + time")
    print("=" * 60)

    now = datetime.now()
    utc_now = datetime.now(tz=timezone.utc)
    print("now():     ", now)
    print("utcnow():  ", utc_now)

    # Construction
    dt = datetime(2024, 3, 15, 9, 30, 0)
    print("datetime(2024,3,15,9,30,0):", dt)

    # From date + time components
    dt2 = datetime.combine(date(2024, 6, 1), time(18, 0, 0))
    print("combine(date, time):", dt2)

    # .date() and .time() accessors
    print("dt.date():", dt.date())
    print("dt.time():", dt.time())

    # Replacing a field
    eod = dt.replace(hour=17, minute=0, second=0)
    print("End of day:", eod)

    print()


# ---------------------------------------------------------------------------
# 4. timedelta arithmetic
# ---------------------------------------------------------------------------

def demo_timedelta():
    print("=" * 60)
    print("timedelta arithmetic")
    print("=" * 60)

    # timedelta can represent days, seconds, and microseconds
    one_week  = timedelta(weeks=1)
    one_day   = timedelta(days=1)
    ninety    = timedelta(days=90)
    two_hours = timedelta(hours=2)

    print("one_week: ", one_week)          # 7 days, 0:00:00
    print("two_hours:", two_hours)          # 0:02:00:00

    # Arithmetic on datetime
    launch_date = datetime(2026, 6, 1, 9, 0)
    one_week_before = launch_date - one_week
    one_week_after  = launch_date + one_week
    print(f"\nLaunch: {launch_date}")
    print(f"1 week before: {one_week_before}")
    print(f"1 week after:  {one_week_after}")

    # Duration between two datetimes
    start = datetime(2024, 1, 1, 8, 0)
    end   = datetime(2024, 1, 3, 17, 30)
    delta = end - start
    print(f"\n{start} to {end}:")
    print(f"  Total seconds: {delta.total_seconds():.0f}")
    print(f"  Days:    {delta.days}")
    print(f"  Seconds: {delta.seconds}")    # seconds within the last day
    hours = delta.total_seconds() / 3600
    print(f"  Hours:   {hours:.1f}")

    # SLA check: was the ticket resolved within 48 hours?
    opened   = datetime(2024, 3, 15, 9, 0)
    resolved = datetime(2024, 3, 17, 10, 30)
    sla_48h  = opened + timedelta(hours=48)
    within_sla = resolved <= sla_48h
    print(f"\nTicket resolved within 48h SLA: {within_sla}")

    print()


# ---------------------------------------------------------------------------
# 5. Formatting (strftime) and parsing (strptime)
# ---------------------------------------------------------------------------

def demo_strftime_strptime():
    print("=" * 60)
    print("strftime (format) and strptime (parse)")
    print("=" * 60)

    dt = datetime(2026, 4, 10, 14, 30, 45)

    # Common format codes
    formats = [
        ("%Y-%m-%d",              "ISO date"),
        ("%Y-%m-%dT%H:%M:%S",     "ISO 8601 datetime"),
        ("%d/%m/%Y",              "UK date"),
        ("%m/%d/%Y",              "US date"),
        ("%B %d, %Y",             "Long date"),
        ("%A, %B %d %Y",          "Full day name"),
        ("%I:%M %p",              "12-hour time"),
        ("%H:%M:%S",              "24-hour time"),
        ("%a %b %d %H:%M:%S %Y",  "Unix ctime style"),
    ]

    print("Formatting 2026-04-10 14:30:45:")
    for fmt, label in formats:
        print(f"  {label:25} {dt.strftime(fmt)}")

    # strptime — parse a string back to datetime
    print("\nParsing strings:")
    test_cases = [
        ("2026-04-10",          "%Y-%m-%d",       "ISO date"),
        ("10/04/2026 14:30",    "%d/%m/%Y %H:%M", "UK datetime"),
        ("April 10, 2026",      "%B %d, %Y",      "Long date"),
        ("2026-04-10T14:30:45", "%Y-%m-%dT%H:%M:%S", "ISO 8601"),
    ]
    for s, fmt, label in test_cases:
        parsed = datetime.strptime(s, fmt)
        print(f"  {label:15}  {s!r:25} -> {parsed}")

    print()


# ---------------------------------------------------------------------------
# 6. Timezone-aware datetimes
# ---------------------------------------------------------------------------

def demo_timezones():
    print("=" * 60)
    print("Timezone-aware datetimes")
    print("=" * 60)

    utc = timezone.utc
    est = timezone(timedelta(hours=-5), name="EST")
    pst = timezone(timedelta(hours=-8), name="PST")
    ist = timezone(timedelta(hours=5, minutes=30), name="IST")

    # Create an aware datetime in UTC
    meeting_utc = datetime(2026, 4, 10, 18, 0, tzinfo=utc)
    print("Meeting UTC:", meeting_utc)

    # Convert to other zones using .astimezone()
    for tz in [est, pst, ist]:
        local = meeting_utc.astimezone(tz)
        print(f"  -> {tz}:  {local.strftime('%Y-%m-%d %H:%M %Z')}")

    # isoformat with timezone
    print("\nisoformat():", meeting_utc.isoformat())
    # 2026-04-10T18:00:00+00:00

    # Unix timestamp <-> datetime
    ts = meeting_utc.timestamp()   # seconds since epoch
    print(f"\nTimestamp: {ts:.0f}")

    recovered = datetime.fromtimestamp(ts, tz=utc)
    print("Recovered from timestamp:", recovered)

    # datetime.fromisoformat handles timezone suffixes (Python 3.11+)
    try:
        dt_iso = datetime.fromisoformat("2026-04-10T18:00:00+00:00")
        print("fromisoformat:", dt_iso)
    except ValueError as e:
        print("fromisoformat error:", e)

    print()


# ---------------------------------------------------------------------------
# 7. Practical patterns
# ---------------------------------------------------------------------------

def demo_practical():
    print("=" * 60)
    print("Practical patterns")
    print("=" * 60)

    today = date.today()

    # --- 7a: Age calculation ---
    def age(birth_date: date) -> int:
        """Calculate age in completed years."""
        today_d = date.today()
        years = today_d.year - birth_date.year
        # Subtract 1 if birthday hasn't occurred yet this year
        if (today_d.month, today_d.day) < (birth_date.month, birth_date.day):
            years -= 1
        return years

    birthday = date(1990, 7, 4)
    print(f"Age of person born {birthday}: {age(birthday)}")

    # --- 7b: Business day arithmetic (skip weekends) ---
    def add_business_days(start: date, n: int) -> date:
        """Add n business days to start (Mon-Fri only)."""
        current = start
        added   = 0
        step    = 1 if n >= 0 else -1
        while added < abs(n):
            current += timedelta(days=step)
            if current.weekday() < 5:   # Monday=0 … Friday=4
                added += 1
        return current

    order_date = date(2026, 4, 10)   # Friday
    delivery   = add_business_days(order_date, 3)
    print(f"\n3 business days after {order_date} ({order_date.strftime('%A')}): "
          f"{delivery} ({delivery.strftime('%A')})")

    # --- 7c: Relative time ("2 hours ago", "in 3 days") ---
    def relative_time(dt: datetime) -> str:
        now   = datetime.now()
        delta = now - dt
        secs  = abs(delta.total_seconds())
        future = delta.total_seconds() < 0

        if secs < 60:
            unit = f"{int(secs)} second{'s' if secs != 1 else ''}"
        elif secs < 3600:
            v    = int(secs / 60)
            unit = f"{v} minute{'s' if v != 1 else ''}"
        elif secs < 86400:
            v    = int(secs / 3600)
            unit = f"{v} hour{'s' if v != 1 else ''}"
        else:
            v    = int(secs / 86400)
            unit = f"{v} day{'s' if v != 1 else ''}"

        return f"in {unit}" if future else f"{unit} ago"

    now = datetime.now()
    for delta_s, label in [(-300, "5 min ago"), (-7200, "2h ago"),
                            (+3600, "in 1h"), (+172800, "in 2 days")]:
        dt = now + timedelta(seconds=delta_s)
        print(f"  {label:15} -> {relative_time(dt)}")

    # --- 7d: Generate a schedule of weekly meetings ---
    start = date(2026, 4, 13)   # next Monday
    print(f"\nWeekly Monday meetings (next 8 weeks):")
    for i in range(8):
        meeting_day = start + timedelta(weeks=i)
        print(f"  {meeting_day.strftime('%A %Y-%m-%d')}")

    # --- 7e: ISO week number for analytics grouping ---
    dates = [date(2026, 1, 1), date(2026, 3, 15), date(2026, 12, 31)]
    print("\nISO week numbers:")
    for d in dates:
        iso = d.isocalendar()
        print(f"  {d} -> week {iso.week:02d} of {iso.year}")

    print()


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    demo_date()
    demo_time()
    demo_datetime_basics()
    demo_timedelta()
    demo_strftime_strptime()
    demo_timezones()
    demo_practical()
