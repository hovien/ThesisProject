## Flask, d3.js & MySQL project

This is a small demo file of a thesis project from HAAGA-Helia University of Applied Sciences. It uses Flask to extract data from a MySQL database and view it on a website. A few simple bar charts are created from the data with the d3.js Javascript library. 

## Code Snippets

The python application queries the MySQL database and passes the data to the Jinja2 template.

```python
def top_users(topic):
    try:
        cursor, conn = connection()
    except Exception as e:
        return(str(e))
    query = ('SELECT user, COUNT(*) FROM '+ topic + ' GROUP BY user ORDER BY COUNT(*) DESC LIMIT 10;')
    cursor.execute(query)
    tup_data = cursor.fetchall()
    data_out = convert_to_json(tup_data)
    return data_out

@app.route('/oil/users/')
def oil_users():
    data = top_users('oil')
    return render_template("oil/users.html", data=data)
```

The data is interpreted as JSON by Jinja2 and a bar chart is created from it with d3.js.

```javascript

var top_users = {{data|tojson|safe}}

var chart = d3.select(".chart")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

var bar = chart.selectAll("g")
    .data(top_users)
  .enter().append("g")
    .attr("transform", function(d, i) { return "translate(" + i * barWidth + ",0)"; });
```

## Motivation

The project was created as a proof of concept for the thesis. The aim was to prove the feasibility of building a market intelligence solution using only open source tools.

## Installation

To use the code it can simply be cloned from here.

## Built With

[Flask](http://flask.pocoo.org/) - web framework

[MySQL](https://www.mysql.com/) - database

[d3.js](https://d3js.org/) - javascript library for visualizations



## Tutorials

The code is largely based on two tutorials:

[Flask & MySQL Tutorial](https://pythonprogramming.net/practical-flask-introduction/)

[D3.js Bar Chart Tutorial](https://bost.ocks.org/mike/bar/3/) 

## License

As the tutorials it is based on, this code is published under [GNU General Public License version 3](https://opensource.org/licenses/GPL-3.0)

