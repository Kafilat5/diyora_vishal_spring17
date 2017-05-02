# INFO 7374 Data Analysis Using Python - Final Project

## Zillow Housing Data Analysis

<img src="http://homevestors.com/wp-content/uploads/ForScreen_RGB_ZillowLogo_White-on-Blue.png">

The data used are as follows:

* From Zillow Data the data such as City's MedianPrice ALL Homes, States House MedianPrice etc. from [Zillow DATA](https://www.zillow.com/research/data/) 
* From the Wikipedia page on college towns is a list of [university towns in the United States](https://en.wikipedia.org/wiki/List_of_college_towns#College_towns_in_the_United_States) which has been copy and pasted into the file ```university_towns.txt```.
* From Bureau of Economic Analysis, US Department of Commerce, the [GDP over time](http://www.bea.gov/national/index.htm#gdp) of the United States in current dollars.
* From Federal Reserve Bank of ST. Louis ,the [30 - Year Fixed Rate Mortgage Average in the United States ](https://fred.stlouisfed.org/series/MORTGAGE30US) of the United States in Percentage. 

*Data Formats*

1. Zillow -CSV File
2. College Towns -txt File
3. Bureau of Economic Analysis, US Department of Commerce(GDP) - CSV File
4. Federal Reserve Bank of ST. Louis (30-Yr Mortgage Rate) - CSV File

## Analysis 1

## Does University towns have their mean housing prices less effected by recessions than Non-University towns?

Data Used:

1. Zillow:-[City_Zhvi_AllHomes.csv](Data/CSV/City_Zhvi_AllHomes.csv)
2. Univeristy town :- [txt file](Data/CSV/university_towns.txt)
3. GDP over time:-[GDP](Data/CSV/gdplev.xls)

**Steps:**

1. <a href="Data/CSV/university_towns.txt">University file</a> file is reading and need to clean the file of University Town. Separate out State name, Town Name and University Name.
2. For GDP find the Recession Start Quater and Recession End Quater
3. Convert [City_Median Price](Data/CSV/City_Zhvi_AllHomes.csv) from number of year to Quaters of Housing Data.
4. Replacing the Abrrievate of States code to State Name of Housing Data.
5. Getting Price of House from Recession Start and Recession End and find the Percentage by(Recession Start- Recession End)/Recession End  whole multiple by 100 of University Town and Non University Town.

## Outputs :

IPython Notebook: <a href="https://github.com/vishal6557/diyora_vishal_spring17/blob/master/final/Analysis1.ipynb">Analysis1</a>

Plot Files:<a href="https://github.com/vishal6557/diyora_vishal_spring17/blob/master/final/Output/Analysis1/Analysis1_University_NonUniversity.png"> Analysis 1 Files</a>

## Unviersity town vs Non University town

<img src="https://github.com/vishal6557/diyora_vishal_spring17/blob/master/final/Output/Analysis1/Analysis1_University_NonUniversity.png">

## Conclusion

In most of the States University town has less price decrease than Non-University Town and from the figure we can conclude than Media Price of house during recession of University town were better than Non-Unviersity as per the Zillow Data Set.

# Analysis 2

### Is their any Relationship between Mortgage Rates and Housing price?

As per the [blog](http://www.bankrate.com/finance/mortgages/rising-rates-lower-house-prices.aspx) and articles. It's a common belief in real estate that house prices are correlated to interest rates. The idea, beloved by homebuyers, is that if mortgage rates rise, prices of homes for sale must fall because otherwise those homes will become less affordable.

Data Used and Input Parameters:

1. Zillow:-[State Median Listing Price](https://github.com/vishal6557/diyora_vishal_spring17/blob/master/final/Data/CSV/State_MedianListingPrice_AllHomes.csv)
2. Federal Reserve Bank[:- 30 - Year Fixed Rate Mortgage](https://github.com/vishal6557/diyora_vishal_spring17/blob/master/final/Data/CSV/MORTGAGE30US_2000_2017.csv)

**Steps:**

1. The CSV of States MedianLisitngprice of All Homes contains $ price from 2010-01 to 2017-02
2. Cleaning data and make the Rows as the Month and Column as state name and Year
3. Mortgage [Average Rates](https://github.com/vishal6557/diyora_vishal_spring17/blob/master/final/Data/CSV/MORTGAGE30US_2000_2017.csv) read as CSV file with 30 Year Fixed Interest.
4. Cleaning and Manipulating Average Mortgage file.
5. Analyzing the relationship between Mortgage and Housing Price in different year and different states.

## Outputs
IPython Notebook: <a href="https://github.com/vishal6557/diyora_vishal_spring17/blob/master/final/Analysis2.ipynb">Analysis2</a>

Plot Files:<a href="https://github.com/vishal6557/diyora_vishal_spring17/blob/master/final/Output/Analysis2"> Analysis2 Files </a>

### Mortgage 30 Year Fix Vs Housing Price

<img src="https://github.com/vishal6557/diyora_vishal_spring17/blob/master/final/Output/Analysis2/Analysis2_California.png">

<img src="https://github.com/vishal6557/diyora_vishal_spring17/blob/master/final/Output/Analysis2/Analysis2_Connecticut.png">

<img src="https://github.com/vishal6557/diyora_vishal_spring17/blob/master/final/Output/Analysis2/Analysis2_Maine.png">

<img src="https://github.com/vishal6557/diyora_vishal_spring17/blob/master/final/Output/Analysis2/Analysis2_Massachusetts.png">

<img src="https://github.com/vishal6557/diyora_vishal_spring17/blob/master/final/Output/Analysis2/Analysis2_New_York.png">

### Conclusion:-

From the plot and as per the blog we can infered that their is no such relationship between mortgage and median house price in any year any state.So It can be infered that mortgage and housing price increase or decrease are irrelavent

# Analysis 3

### Median Price Analysis of City Using Zillow dataset

Data used:-
1. Zillow Data [City Median ListingPrice](https://github.com/vishal6557/diyora_vishal_spring17/blob/master/final/Data/CSV/City_MedianListingPrice_AllHomes.csv)

**Steps:**

1. Read the CSV file and find out the Total Change from 2017-02 to 2010-01
2. Making new column of Perctange change ,Year percent change and Year change
3. Plotting the Graph Mean total Change Grouped By State, City and Metro

## Outputs

IPython Notebook: <a href="https://github.com/vishal6557/diyora_vishal_spring17/blob/master/final/Analysis3.ipynb">Analysis3</a>

Plot Files:<a href="https://github.com/vishal6557/diyora_vishal_spring17/blob/master/final/Output/Analysis3"> Analysis3 Files </a>

### Median Price Analysis of City

<img src="https://github.com/vishal6557/diyora_vishal_spring17/blob/master/final/Output/Analysis3/Analysis3_Mean_City.png">
<img src="https://github.com/vishal6557/diyora_vishal_spring17/blob/master/final/Output/Analysis3/Analysis3_Mean_Metro.png">
<img src="https://github.com/vishal6557/diyora_vishal_spring17/blob/master/final/Output/Analysis3/Analysis3_Mean_State.png">
<img src="https://github.com/vishal6557/diyora_vishal_spring17/blob/master/final/Output/Analysis3/Analysis3_Mean_Per_City.png">

# Analysis 4

## Is their is any relationship between Gross domestic product(GDP) vs Housing Price?

Could housing have dramatic effects on the economy of a nation? This question was examined in this [study](http://www.aabri.com/manuscripts/10490.pdf). The
literature review along with the results of this study’s correlation analysis provides convincing
evidence that a strong relationship exists between the two variables.<br>

Data Input:-

1. Zillow Data Median Price CSV [State](https://github.com/vishal6557/diyora_vishal_spring17/blob/master/final/Data/CSV/State_Zhvi_AllHomes.csv)
2. Gross Domestic Product(GDP) CSV [By State Quaterly](https://github.com/vishal6557/diyora_vishal_spring17/blob/master/final/Data/CSV/GDP_State_Quaterly.csv)

** Steps:**

1. Read the Zillow and GDP CSV file and analyze gdp vs price from 2008-2016.
2. Convert Months to Quater Period to as the GDP is in Quaters and to do Comparisons between them.

## Outputs

IPython Notebook: <a href="https://github.com/vishal6557/diyora_vishal_spring17/blob/master/final/Analysis4.ipynb">Analysis4</a>

Plot Files:<a href="https://github.com/vishal6557/diyora_vishal_spring17/blob/master/final/Output/Analysis4"> Analysis 4 Files </a>

### Median Price Analysis of City

<img src="https://github.com/vishal6557/diyora_vishal_spring17/blob/master/final/Output/Analysis4/Analysis4_New_York.png">
<img src="https://github.com/vishal6557/diyora_vishal_spring17/blob/master/final/Output/Analysis4/Analysis4_California.png">
<img src="https://github.com/vishal6557/diyora_vishal_spring17/blob/master/final/Output/Analysis4/Analysis4_Alabama.png">
<img src="https://github.com/vishal6557/diyora_vishal_spring17/blob/master/final/Output/Analysis4/Analysis4_Massachusetts.png">

### Conclusions:-

From the plot we can see that their is relationship between GDP and Median House Price when the Price increases GDP is also increase and Price decreases GDP also decreases for all the above states.

# Analysis 5

### Median Rental Price of All Home By State(Map Plot) and County wise heat map of Median Sold House Price of All Homes

Data Used and Input Parameters:

1. Zillow:-[State Median Rental Price](https://github.com/vishal6557/diyora_vishal_spring17/blob/master/final/Data/CSV/State_MedianRentalPrice_AllHomes.csv)
2. Zillow:-[County Median ListingPrice](https://github.com/vishal6557/diyora_vishal_spring17/blob/master/final/Data/CSV/County_MedianListingPrice_AllHomes.csv)

**Steps:**

1. Read the Zillow data from CSV of Median Rental Price and Plot it Using Plotly offline US Map
2. Heat Map of the file County Median House Price

## Outputs

IPython Notebook: <a href="https://github.com/vishal6557/diyora_vishal_spring17/blob/master/final/Analysis5.ipynb">Analysis5</a>

Plot Files:<a href="https://github.com/vishal6557/diyora_vishal_spring17/blob/master/final/Output/Analysis5"> Analysis5 Files </a>

### We can see from Map that the New York State has Average highest rental rate ,California and so on.

<img src="https://github.com/vishal6557/diyora_vishal_spring17/blob/master/final/Output/Analysis5/Analysis5_State.png">

## Heat Map of the sold house price of January 2017 by county. 

<img src="final/Output/Analysis5/bokeh_plot (2).png">



