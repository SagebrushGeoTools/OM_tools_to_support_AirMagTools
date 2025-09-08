# Goals: 
### Check 1) diurnal, 2) speed, 3) drape surface, and 4) noise levels  

## Inputs:  
- DEM/DTM – project DEM or DTM (raster)
- Channel mapping (optional)
- Drape surface or terrain clearance surface
    - contract 3D flight surface to ensure tie lines and production lines are at same elevation (raster)
    - could be channel or raster
- Drape deviation
    - for mag will be allowed elevation deviation above and below target
    - may be a tolerance above a target surface
    - may be 0
- Drape length
    - max distance allowed for out of spec in meters
- Data Hz.
    - Sample rate of data or read from UTC time
- Speed
    - contract acquisition speed in meters per second
- Diurnal spec 1
    - Chord length in seconds and nT deviation allowed
- Diurnal spec 2
    - Chord length in seconds and nT deviation allowed

## Visualization inputs:
- Diurnal = view the whole line length
- Drape/Speed = view ¼ to whole line depending on monitor and line length
- Noise QC = view 100 readings per Hz, 4000 readings for 40 Hz

## Drape Check:
1. Sample DEM and Drape into the database if not already done so
2. Calculate out-of-spec surface (EM) or surfaces (Mag-Rad)
3. Review profiles and make a report of out-of-spec lines

## Speed check:
1. Calculate ground speed from X, Y, and sample rate
2. Review speed profiles for issues such as steps
3. Calculate average speed
<img width="468" height="279" alt="image" src="https://github.com/user-attachments/assets/fa01590f-5120-40d5-9cda-6d8c06bd595d" />

## Diurnal check:
1. Calculate deviations from chord(s)
2. Review profiles of deviations
3. Summarize deviations by flight and line
<img width="468" height="295" alt="image" src="https://github.com/user-attachments/assets/4d0076c9-95ff-46cf-a2bc-7c04b14507e4" />

## Noise and compensation check:
1. Visually inspect compensated and uncompensated data
2. Calculate 4th or 8th difference
3. Use a combination of filters or a B-Spline to isolate high-frequency noise.  Ideally, turning the filter off in high gradient areas
4. Visually inspect residual noise
<img width="468" height="297" alt="image" src="https://github.com/user-attachments/assets/1c2ffd42-47eb-4a73-8583-8a7135bb31f9" />

## Example QC report:
<img width="468" height="100" alt="image" src="https://github.com/user-attachments/assets/61116f49-4e6a-423d-b6ac-3c9fac62ba55" /> 

## Tie line QC:
- Check the elevation difference of tie line crossings by sampling “L” lines to “T” lines and vice versa

## Output data Files:
- single_line_with_outputs.csv – single line of data with processed outputs
- single_line_with_outputs_readme.csv – channel guide
- full_test_data.csv – multi-line test data
