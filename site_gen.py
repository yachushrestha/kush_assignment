'''

gen_home is index.html which contains target links to different pages containing
information related to fatalities categorized by age, speed limits, vehicle types etc

The page contains information in tables form, which can be used to infer and interpret
which of the years their were most casualaties as well as at which speed.

## HTML PAGES: ##

Index.html
Page1.html
Page2.html
Page3.html
Page4.html

'''


def gen_home():
    with open('index.html', 'w') as f:
        f.write("<!DOCTYPE html>"
                "<html>"
                "<head>"
                '<link rel="stylesheet" href="styles.css"></link>'
                "</style>"
                "</head>"
                "<body>"
                "<title>Fatalities Information</title>"
                "<body>"
                "<a href=""page1.html"">Fatalities By Age</a>"
                "<a href=""page2.html"">Fatalities By Speed</a>"
                "<a href=""page3.html"">Fatalities By Year</a>"
                "<a href=""page4.html"">Fatalities By Day</a>"
                "<h1 style=color:white>ABOUT</h1>"
                "<P style=font-size:20px>The site provides information about fatalities.</p>"
                "</body>"
                "</html>"
                )


def table_heading_generator(table_heading):
    lst = ['<tr>']
    count = list(range(len(table_heading)))

    for i in count:
        lst.append('<th>' + table_heading[i] + '</th>')

    lst.append('</tr>')

    return lst


def table_content_generator(table_content):
    lst = []
    for k, v in table_content.items():
        lst.append('<tr>')
        lst.append('<td>' + str(k) + '</td>')
        lst.append('<td>' + str(v) + '</td>')
        lst.append('</tr>')
    return lst


def generateHTML(content_var, page_name, page_heading, heading_tag):
    heading = table_heading_generator(table_heading=heading_tag)
    content = table_content_generator(table_content=content_var)

    with open(page_name, 'w') as j:
        j.write('''<!DOCTYPE html>
                <html>
                <head>
                <style>
                h2 {
                    text-align: center;
                    color: white;
                }
                a:link, a:visited {
                    background-color: grey;
                    color: white;
                    padding: 20px 40px;
                    text-align: center;
                    text-decoration: none;
                    display: inline-block;
                }

                a:hover, a:active {
                	background-color: black;
                }

                body {
                    background-image: url("abc.jpg");
                    background-color: #cccccc;
                }
                table {
                    font-family: arial, sans-serif;
                    border-collapse: collapse;
                    width: 100%;
                }

                td, th {
                    color: white;
                    text-align: left;
                    padding: 8px;
                }
                </style>
                </head>
                <body>
               <a href="index.html">Home</a>
                ''')
        j.write('<h2>{}</h2>'.format(page_heading))

        j.write('<table>')
        j.write(''.join(heading))
        j.write(''.join(content))
        j.write('</table>')
        j.write('</body>')
        j.write('</html>')


if __name__ == "__main__":
    gen_home()
    days = ("Monday", "Tuesday", "Wednesday",
            "Thursday", "Friday", "Saturday", "Sunday")
    with Fatalities() as my_obj:
        fatals_per_year = {}
        days_fatal = {k: my_obj.get_by_day(day=k) for k in days}
        for y in range(1989, 2019):
            fatals_per_year[y] = my_obj.get_by_year(y)

        generateHTML(my_obj.get_impact_age(), 'page1.html',
                     page_heading="Impact By Age", heading_tag=["Age", "Fatalities"])

        generateHTML(my_obj.get_impact_speed(), 'page2.html',
                     page_heading="Impact By Speed", heading_tag=["Speed", "Fatalities"])

        generateHTML(fatals_per_year, 'page3.html',
                     page_heading="Fatalities By Year", heading_tag=["Year", "Fatalities"])

        generateHTML(days_fatal, 'page4.html',
                     page_heading="Fatalities By Days", heading_tag=["Days", "Fatalities"])
