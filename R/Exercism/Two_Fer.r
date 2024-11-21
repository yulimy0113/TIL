# Your task is to determine what you will say as you give away the extra cookie.
# If you know the person's name (e.g. if they're named Do-yun), 
# then you will say: "One for Do-yun, one for me."
# If you don't know the person's name, 
# you will say you instead. "One for you, one for me."

two_fer <- function(input=FALSE) { # You can also put "you" instead of FALSE to make it more simple!
  if (input == FALSE){
    return("One for you, one for me.")
  }
  else{
    return(paste("One for ", input, ", one for me.", sep = ""))
  }
}
