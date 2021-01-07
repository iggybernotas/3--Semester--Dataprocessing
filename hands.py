from datetime import datetime, timedelta
import psycopg2
import gpxpy
import gpxpy.gpx
#connection to db
conn = psycopg2.connect(dbname="postgres", user="postgres", password="password", host="127.0.0.1")
cur = conn.cursor()

#add timestamp and timedelta, emulating passing time
timestamp = datetime.strptime("2020-11-05 19:09:16.137210", "%Y-%m-%d %H:%M:%S.%f")
delta = timedelta(0, 2.2)
#open gpx file
gpx_file = open('GraphHopper.gpx', 'r')
#parse to get gps cord
gpx = gpxpy.parse(gpx_file)
#loop thru seperate crod and save it to db
for track in gpx.tracks:
    for segment in track.segments:
        print(len(segment.points))
        for point in segment.points:
            print(point.latitude, point.longitude)
            sql = f"""
            INSERT INTO public.hands (
            "h1","h2","time","coord") VALUES (
            '20'::integer,'10'::integer,'{timestamp}'::time with time zone,  '{{{point.latitude}, {point.longitude}}}'::numeric[])
            """
            print(sql)
            cur.execute(sql)
            timestamp += delta
        
conn.commit()