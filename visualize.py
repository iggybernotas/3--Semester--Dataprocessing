import matplotlib.pyplot as plt
import matplotlib.ticker
import psycopg2
#connect to db
conn = psycopg2.connect(dbname="postgres", user="postgres", password="password", host="127.0.0.1")
cur = conn.cursor()
#selecting and fetching data  
cur.execute('SELECT * FROM public.heart ORDER BY "time" ASC')
bpm = cur.fetchall()
#transposing 2d list & swapping rows with columns `
bpm = list(zip(*bpm))

#blank page for plots
fig = plt.figure(figsize=(20,20))
#function to create plot
def plot(i, num, xaxis, data):
    if i == 2:
        xaxis = [str((str(xval[0]), str(xval[1]))) for xval in xaxis]
    #position on the grid
    pos = 2*100+10+i
    #subplot
    ax1 = fig.add_subplot(pos)
    #subplot title
    ax1.set_title("bpm")
    #created on the page with "x" as time stamps and "y" as data
    ax1.xaxis.set_major_locator(matplotlib.ticker.MaxNLocator(nbins=5))
    ax1.plot([str(time) for time in xaxis], data)

#looping individual conditions
plot(1, len(bpm), bpm[1], bpm[0])
plot(2, len(bpm), bpm[2], bpm[0])

#window size
plt.subplots_adjust(hspace=1)
#visualize on the screen
plt.show()