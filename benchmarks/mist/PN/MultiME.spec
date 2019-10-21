vars
    x0 x1 x2 x3 x4 x5 x6 x7 x8 x9 x10 x11

rules
    x0 >= 1,
    x1 >= 1,
    x2 >= 1 ->
		    x0' = x0-1,
		    x2' = x2-1,
		    x3' = x3+1;

    x0 >= 1,
    x1 >= 1,
    x2 >= 1 ->
		    x0' = x0-1,
		    x1' = x1-1,
		    x4' = x4+1;

    x3 >= 1 ->
		    x0' = x0+1,
		    x2' = x2+1,
		    x3' = x3-1;

    x4 >= 1 ->
		    x0' = x0+1,
		    x1' = x1+1,
		    x4' = x4-1;


    x0 >= 1,
    x5 >= 1,
    x6 >= 1 ->
		    x0' = x0-1,
		    x6' = x6-1,
		    x7' = x7+1;

    x0 >= 1,
    x5 >= 1,
    x6 >= 1 ->
		    x0' = x0-1,
		    x5' = x5-1,
		    x8' = x8+1;

    x7 >= 1 ->
		    x0' = x0+1,
		    x6' = x6+1,
		    x7' = x7-1;

    x8 >= 1 ->
		    x0' = x0+1,
		    x5' = x5+1,
		    x8' = x8-1;

    x9 >= 1 ->
		    x9' = x9-1,
                    x10' = x10+1;
 
    x10 >= 1 ->
                    x10' = x10-1,
                    x11' = x11+1;

    x11 >= 1 ->
                    x11' = x11-1,
                    x10' = x10+1,
                    x0'  = x0+1;


init
    x0 = 0, x1 = 1, x2 = 1, x3 = 0, x4 = 0, x5 = 1, x6 = 1, x7 = 0, x8 = 0, x9 = 1, x10 = 0, x11 = 0

target
    x3 >= 1, x4 >= 1
    x3 >= 2
    x4 >= 2
