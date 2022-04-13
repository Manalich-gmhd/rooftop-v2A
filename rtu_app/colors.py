def get_quality_score(v,graf):
  #FFEB3B";  //yellow
  #FFC107"; //amber
  #FF9800"; //orange
  #FF5722";//deep orange
  #F44336";//red	
  #4CAF50";//green	
  if graf:
    res = 'rgba(127,127,127, 0.75)'
  else:
    res = '#7F7F7F'
    
  if ((v >= 0) and (v < 60)):
    if graf:
      res = "rgba(242,156,51, 0.75)"
    else:
      res = "#F29C33"
  elif ((v >= 60) and (v < 80)):
      if graf:
        res = "rgba(249,201,51, 0.75)"
      else:
        res = "#F9C933"
  elif (v >= 80):
      if graf:
        res = "rgba(73,206,76, 0.75)"
      else:
        res = "#49CE4C" #green	
  return res


def get_index_color(v, index):
  if (index == 1):
    return get_quality_score(v, False)
