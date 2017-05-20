library(shiny)
library(leaflet)

# Define UI for application that draws a histogram
shinyUI(fluidPage(
  
  # Application title
  titlePanel("Hello Shiny!"),
  
  # Sidebar with a slider input for the number of bins
  sidebarLayout(
    sidebarPanel(
      selectInput("selectStart", label = h3("Select start point"), 
                  choices = list("Factory Berlin", "Berlin Hbf"), selected = 1)
    ),
    
    # Show a plot of the generated distribution
    mainPanel(
      fluidPage(
        leafletOutput("mymap"),
        p(),
        actionButton("recalc", "New points")
      )
    )
  )
))