1. In order to select the default [text interpreter](https://es.mathworks.com/help/matlab/ref/matlab.graphics.primitive.text-properties.html#budt_bq-1_sep_shared-Interpreter) in all tick labels from here:
```matlab
set(groot, 'defaultAxesTickLabelInterpreter', 'none')
```
To reverse to the default interpreter use `'remove'` instead of `'none'`

- More information about default values in [this link](https://www.mathworks.com/help/matlab/creating_plots/default-property-values.html) 
- More info about `groot` (Graphics root object) in [this link](https://www.mathworks.com/help/matlab/ref/groot.html)

2. Disable plot/figure generation in execution (image not shown on screen):
```matlab
set(groot,'defaultFigureVisible','off')
```
More info in [this link](https://es.mathworks.com/matlabcentral/answers/160265-is-it-possible-to-disable-plot-figure-generation-in-an-entire-script)
