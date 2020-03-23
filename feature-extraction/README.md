# Feature Extraction

**Lib Name** - aud-fea  

**Includes** --  

Import:  
import fea  
 
**Window**:  
eg:  
var = fea.Win(aud = var{type = numpy.array}, choice = ("ham" or "rect"){type = str})  
Descreption: ham - hamming window, rect - rectangular window  

**Short Time Energy**:-  
eg:  
var = fea.Short_Time_Energ(aud = var{type = numpy.array} , window = var{type =numpy.array})

**Normalised Short Time Energy**:-  
eg:  
var = fea.Norm_Short_Time_Energ(aud = var{type = numpy.array} , window = var{type =numpy.array})

**Short Time Magnitude**:-  
eg:  
var = fea.Short_Time_Mag(aud = var{type = numpy.array} , window = var{type =numpy.array})

**Normalised Short Time Magnitude**:-  
eg:  
var = fea.Norm_Short_Time_Mag(aud = var{type = numpy.array} , window = var{type =numpy.array})

**Zero Crossing Rate**:-  
eg:   
var = fea.Zero_Crossing(aud = var{type = numpy.array} , window = var{type =numpy.array})
