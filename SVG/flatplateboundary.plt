# png
#set terminal "png"
#set output "boundary.png"

# eps
set terminal postscript eps 
#set size 1.0,1.0
set output 'flatplateboundary.eps'

set title "Flat Plate Boundary Conditions" font "Arial, 14"


set border lw 2 lc rgb 'black 

set xrange [-0.5:2.1]
set yrange [-0.1:1.1]
set xlabel "X" font "Arial, 14" offset 0, 0.5 
set ylabel "Y" font "Arial, 14" offset 2.0, 0

set obj 1 rect from -0.3333333,0 to 2,1 lw 2

set arrow from 0,0 to 0,0.05 nohead

set arrow from -0.33333,0.025 to 0,0.025 heads
set arrow from -0.14,0.1 to -0.14,0.025 head
set label 1 at -0.05,0.12
set label 1 "symmetry" center font "Arial, 14"

set arrow from 0,0.025 to 2,0.025 heads
set arrow from 1.0,0.1 to 1.0,0.025 head
set label 2 at 1.0,0.12
set label 2 "solid wall" center font "Arial, 14"

set arrow from 0.833333,0.9 to 0.833333,1.0 head
set label 3 at 0.833333,0.88
set label 3 "farfield" center font "Arial, 14"

set arrow from 1.8,0.5 to 2.0,0.5 head
set label 4 at 1.78,0.5
set label 4 "outlet" right font "Arial, 14"

set arrow from -0.133333,0.5 to -0.3333333,0.5 head
set label 5 at -0.133333,0.5
set label 5 "inlet" left  font "Arial, 14"

set label 6 at 0.833333,0.6
set label 6 "<M_a = 0.2, T_{ref} = 300 K>" center font "Arial, 14"

set label 7 at 0.833333,0.4
set label 7 "<R_e = 5e6, L = 1.0>" center font "Arial, 14"

plot -0.1 notitle
