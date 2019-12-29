Slic3r A10M options
===================

## General notes

This profile is for genuine Slic3r.org slicer development version only, which you can download it here: https://dl.slic3r.org/dev/win/

**All settings are for UNTOUCHED printer as you got it from manufacturer.** 

All values are calculated to 340 extruder steps as in A10M factory firmware. If you have calibrated values or use 430 steps, set it to factory  values.

Printers need to be tightened after shipping shocks. Use only manual screwdriver to tighten all screws except the wheels at the right side of X arm. 

Hotbed springs need to be slightly tightened too, so you could put Z-axis switch to 1-2mm lower position for greater stiffness.

Printing speed is limited by volumetric speed to 10mm3/s. Physical limit of path extruder gear - hotend tip is about 13-15mm3/s. Because my extruder lever is broken after few weeks, I was print another and use bigger spring. Your gears should be clean, no splinters from filament, only small amount of white dust at both sides of saw wheel and filament way is mirrorish clean.


## Slicer picked options
 
#### Advanced
- Infill/perimeter overlap - if your long bridge hairs are falling from edges, use bigger value
- XY Size  Compensation - compensation if you need to fit together (0.05mm mean 0.2mm difference in tolerance of joined diameters)

#### Extruders
options for dual material or color prints only

#### Extrusion width
Use both values to fit your design or use "auto" value together with Fill gaps option checked.

#### Infill
- Infill patterns - Hilbert is for great adhesivity of bottom side. Other use as you want.
- FIll angle set to 90 if you want different bridge or top layer way.
- Fill density - use bigger values to make it strength
- FIll gaps - worse print quality, better strength
- Combine Infill - for speed-up prints
- Infill before perimeters - use it if you need as much exact size of diameters etc.
- Only infill where needed - unchecked is for strong prints, checked acts as internal support material
- Solid infill treshold - about 5-10 for strong vertical  sticks, 0 for selected % infill only.  
- Solid infill every - is for better strength

#### Layers
- Use adaptive slicing - for models with many skews, Quality 75% is good for many details, 35% is good few details
- Avoid crossing - if on, then printing quality of small details is much worse, leave it off (maybe disappear in futire)
- External perimeters First - if you want to have as much exact surfaces as possible.
- Only retract when... - in rare case of simple objects it will spedd-up print

#### Speed
- bigger speed = worse detail, worse adhesivity

## Dual colour print configuration for bucket and switching filaments (no mixing at the moment)
- Print: HQ/Speed
- Filament: DUAL
- Printer: DUAL

## Vase mode prints guide
#### Printer
- Simple Vase for simple vase models without retractions
- Strong if object is not slashed
- HQ/Speedy if vase is relative complex object with needed retractions
#### Filament
- vase HD - for high details prints
- vase BLACK - for asphaltic black colour only
- Light Speedy - for all other colours - if it does high-temp artifacts, use dDark Speedy or Dark only.

## Complex objects guide
#### Print settings
- HQ/AUTO - select what is better for your model (see Preview)
- Speedy Gonzales is faster print
- Speedy McQueen is fastest print as possible, quality is not measure
- Vase Paper-thin - if you need paperweight vase mode figures
#### Filaments
- Speed - for speed prints
- Dark/Light - about filament colour
- CARDS - for thin cards or very tiny or thin objects with small height - note that strongness is much worse.
#### Printer
- STRONG - for strong objects, it does not have height temperature profile as others do. Reccomended with LightSpeedy filament settings, but quality is lower due high-temp artifacts while retraction
- HQ/Speed - correspond with Print settings
