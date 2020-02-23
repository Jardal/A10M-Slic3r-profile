Slic3r A10M 3D printer profile
==============================

This is content of the folder and file structure from c:\Users\[yourname]\AppData\Roaming\Slic3r 

This profile is for genuine Slic3r.org slicer development version only, which you can download it here: https://dl.slic3r.org/dev/win/
Note that Slic3r need a lot of power to display itself, it will display slowly on machines with Atom or similar CPU.

**All settings are for UNTOUCHED printer as you got it from manufacturer.** 
Mine printer is with black SiC surface glass which is not need to use glue or something else. Sticking is not as good as with glue, but you easily take printed parts if hotbed is under 40°C.

All values are calculated to 340 extruder steps as in A10M factory firmware. If you have calibrated values or use 430 steps, set it to factory  values.

Printing speed is limited by volumetric speed to 10mm3/s. Physical limit of path extruder gear - hotend tip is about 13-15mm3/s. Because my extruder lever is broken after few weeks, I was print another and use bigger spring. Your gears should be clean, no splinters from filament, only small amount of white dust at both sides of saw wheel and filament way is mirrorish clean.
Do not use Speedy profiles if you are unsure about extruder driver status. Critical value of whole path is about 4-6mm3/s, so if you are under this limit, your prints are in higher quality. Values you can check in gcode output.

There is unique **implemented height-temperature response** which is good for free-air printing. I was discovered right values while printing of skewed vase mode complex models. But result is not as strong as high temperature prints.  

## Slicer picked options
 
#### Advanced
- Complete individual objects - for multiple printing objects - need 37mm space between, pay attention on XY axis when place objects with height over 27mm
- Infill/perimeter overlap - if your long bridge hairs are falling from edges, use bigger value
- XY Size  Compensation - compensation if you need to fit together (0.05mm mean 0.2mm difference in tolerance of joined diameters)

#### Extruders
options for dual material or color prints only
- Regions... overlap - give 0.05 to glue objects together or -0.25 or more to make separate objects

#### Extrusion width
Use values to fit your design or use "auto" value together with Fill gaps option checked. A10M AUTO have "auto" or "default" values enabled at all.
**External perimeters**
- upright and exact sizes are best with 0.42mm width
- universal or skewed design is best with 0.52mm but did not want exact holes (are smaller) and size in X-Y is slightly (way) bigger
- exact sizes or skewed vase mode 0.6mm (exact with with xy compensation -0.08mm)
- upright vase mode could be up to 0.8mm for better strongness  

#### Infill
- Infill patterns - Hilbert is for great adhesivity of bottom side. Other use as you want.
- FIll angle set to 90 if you want different bridge or top layer way.
- Fill density - use bigger values to make it strength, but 10% and 3 shells is enough
- FIll gaps - worse print quality, better strength, did not use it at very small or complex tiny detail objects
- Combine Infill - for speed-up prints, less strength if values >1
- Infill before perimeters - use it if you need as much exact size of diameters or when infill destroy perimeters (ABS); use low infill only (10%)
- Only infill where needed - unchecked is for strong prints, checked acts as internal support material - speed-up prints, less strength (about 20% less)
- Solid infill treshold - about 5-10 for strong vertical  sticks, 0 for selected % infill only.  
- Solid infill every - is for better strength, but not as much. Use about 10 if you have horizontal holes for big screws.

#### Layers
- Use adaptive slicing - for models with many skews, Quality 75% is good for many details, 35% is good few details
- layer height - 0.3mm is maximum, for some colours (silver) 0.28. Thinner layer does not as much nicer finish as you think, but 0.2 are much stronger than 0.3. More height, more External perimeter width.
- Avoid crossing - if on, then printing quality of small details is much worse, leave it off (maybe disappear in future - future is now)
- External perimeters First - if you want to have as much exact surfaces as possible. Disable it at very small pieces if you dont want to use brim.
- Only retract when... - disable it in rare case of simple objects or if you print infill only without perimeters (aka negative vase mode), enabled for spedd-up print
- Bottom/Top layers - these values are as minumum, did not use less. If you print with thin layers, increase both values. More layers = more strength
- Perimeters - 2 is too low (big impact to quality, about 20% less strength), 3 is nice. More perimeters = more strength about 2-3% only and worse quality of details, but holes with big screws you can tight more with 4-5 and 40% infill

#### Speed
- External - bigger speed = worse detail, worse strength
- First - if you print tiny objects, use lower value (10) for better adhesivity. At extra large objects it prevents corner warping.

## Complex objects guide
#### Print settings
- HQ/AUTO - select what is better for your model (see Preview)
- Speedy Gonzales is faster print
- Speedy McQueen is fastest print as possible, quality is not measure
- MULTI PLY 2,5mm is profile for thin multiple objects up to 2,5mm, printed in completation sequence, not at one. My A10M have vertical space between nozzle tip and PLA cooling fan mouth 2,5mm. Measure your printer first! Use with CARDS filament profile and HQ/AUTO printer.
#### Filaments
- Speed - for speed prints
- Dark/Light - about filament colour
- CARDS - for thin cards or very tiny or thin objects with small height - note that strongness is much worse. If you print a boomerang, use Speedy Gonzales Light + STRONG
- STRONG - for strong, lower complexity  objects; Set Infill/perimeter overlap to 60%, xy size -0.015, perimeters width 0.52 and 0.56, fill gaps on; How it is different from LightSpeedy: fan is off, fatter extrusion multiplier, limited volumetric speed.
#### Printer
- STRONG - for strong objects, it does not have height temperature profile as others do. Reccomended with LightSpeedy or STRONG filament settings, but quality is lower due high-temp artifacts while retraction
- HQ/Speed - correspond with Print settings

## Vase mode prints guide
#### Print settings
- vase HQ for highest quality of print
- vase Speedy Gonzales is fast print
- Vase Paper-thin - if you need paperweight vase mode figures
#### Filament
- vase HD - for high details prints
- vase BLACK - for asphaltic black colour only
- Light Speedy - for all other colours - if it does high-temp artifacts, use dDark Speedy or Dark only.
#### Printer
- Simple Vase for simple vase models without retractions
- Strong if object is not slashed
- HQ/Speedy if vase is relative complex object with needed retractions

## Dual colour print configuration
For bucket and switching filaments (no mixing at the moment)
- Print: HQ/Speed
- Filament: DUAL
- Printer: DUAL

## Tricks
- print models near back of build plate, it will save your cables
- try to print "body" of the vase model by setting perimeters to zero.
- objects could be printed as vase too if you need it for measuring if it will fit to. If object is multipart, export whole bed from Slic3r as STL and import this file instead
- Support is needed only in rare case, adaptive mode prints from about 10 deg withut it.
- Microsoft 3D Builder is not bad for editing models. But Tinkercad is better for exact construction work.
- Geeetech in download section have Color Mixer software, try it. It supplies mixer from control Panel, but way better.
- if you need dual coloured part, go to Settings button...
- Each gcode file from Slic3r contain at the end whole printing configuration which could be imported to Slic3r again
- Each gcode file contain at the begin all settings what you set it at the right panel for future reference (and you did not need to make printscreen with settings)
- Slic3r remember settings and you want to begin with defaults? Simply edit file slic3r.ini and delete row with last_output_path and whole sections Presets and Recent.
- Dual colour print should be used without filament cleaning, but remember that to change colour it need about 25mm in extruder (ie., 25-50 cm of transient colour to fully change colour). You slould set same value (2 for left extruder) to Infill and Perimeter extruder in Extruders section
- You can check gcode health with Pronterface http://kliment.kapsi.fi/printrun/ . just associate gcode files with Pronterface... See Internet Archive if link disappeared: https://web.archive.org/web/20191031020314/http://kliment.kapsi.fi/printrun/
- Strongest pieces you will get with layers 0.2 or 0.15mm, about 10% less with thinner print and about 50% less with 0.3mm
- Infill does not have such impact on strongness as you think. 3 perimeters and 10% infill are about 10% less than 100% infill

## Notes about material
**Profile is for ABS only**. Best colours for quality printings are white, yellow, green, light gray. Bad colors are silver, black. Use plastics without smell, they are way better than fume filaments.

Remember, that ABS is not able to print curves in free air as PLA wit appropriate cooling blower, bridges only.
 
## How to make good printer
### Tighten it all
Printers need to be tightened after shipping shocks. Use only manual screwdriver to tighten all screws and wheels except the wheels at the right side of X arm. Hotbed springs need to be slightly tightened too, so you could put Z-axis switch to 1-2mm lower position for greater stiffness. 
### Lubricate it all
Use gun oil to lubricate bearings and lithium vaseline to the Z-axis rod and gears in the extruder (except saw wheel of course).
### Do it at the first
- filament filter
- dual colour bucket
- extruder lever
- Cable pathway helper
- LED lightning in the top-dovn V-slot(2x 10cm LED 12V strip in series), powered from PSU, but you must know what you do, otherwise your printer will be burned. Possible version for "civilians": https://www.thingiverse.com/thing:4089189
- fan silencer (note that for 2019/10 version is needed only one for PSU)
- use plastic shopping bag as dust shield for top of printer with filament spools
- cover hotbed at least with sheet of paper if you leave your printer cold 

...Files, images or links will be added later, stay tuned. 
 
## Repair parts
- Extruder Lever for print in Repair parts folder (lever which I was edited but forged from where it is - if you are original author, leave a note here)
- Extruder Nozzle tip
- Fittings
- PTFE (teflon) tube
- V-slot wheels
- GT2 belt
- Thermistor in glass B3950 100k 1m
- 40W/24V heater element 30mm (or 20mm)
- 3010 24V fans
- 4010 24V blowing fan
- PLA fan duct for 4010 fan
- 4010 24V system unit fan

## Tuning parts
- Waste bucket for dual colour prints
- Bed heihgt wheels
- filament filter
- Thumb wheels for Titan extruder lever spring
- Cable pathway helper
- fan silencer for PSU - simply resize it to 168% in slicer and tight it with one screw only. It is about 12% oversized because it is exhaust side - https://www.thingiverse.com/thing:2988448 
  Of course you can try newer versions with phase invertors https://www.thingiverse.com/thing:2988448
- fan silencer for system unit (not for 2019/10+ model) with 8010 12V fan and mini DC/DC step-down module
- extruder support for tall prints 
- Back-up UPS 700VA or more (not each 500VA will work)
- 4020 24V blowing fan with PLA fan duct and extended drive capability to 0-255 PWH with arduino+NPN (DIY). Small flow is needed for ABS, high for PLA, but small flow 35% is too high for ABS with bigger fan. 

## Servicing Printer
- Clogged bowden - https://www.youtube.com/watch?v=uKxPIGal74E
- What you often need to do if you does not have filament filter - https://www.youtube.com/watch?v=hOKSaBrxTDs
- Attention! thermistors are connected from 5V to Ain instead of Ain to GND. Easy to burn out mainboard!

## Main differences A10M over generic CR10 printer
- modularized system unit - you can replace stepper driver
- you did not tunings - are already done

## Wizard
It is possible to make application which will create right configuration based on questions and answers. Or Machine learning/AI based analysis of object. You can do it.

## Missing options in Slic3r
with settings for A10M with black glass
- Printer/Extruder/Wipe + [x] do not wipe first layer  [] do not wipe top layer  [x] do not wipe short tracks below [3 mm]
- Print/Infill/Print gaps + [x] do not fill gaps on first layer  [x] do not fill gaps on top layer
- Print/Layers/External perimeters first + From layer [3] 

with settings for A10 with PEI sheet
- Printer/Extruder/Wipe + [x] do not wipe first layer  [x] do not wipe top layer  [x] do not wipe short tracks below [3 mm]
- Print/Infill/Print gaps + [x] do not fill gaps on first layer  [x] do not fill gaps on top layer
- Print/Layers/External perimeters first + From layer [2] 



...formated by using https://medium.com/swlh/how-to-make-the-perfect-readme-md-on-github-92ed5771c061
