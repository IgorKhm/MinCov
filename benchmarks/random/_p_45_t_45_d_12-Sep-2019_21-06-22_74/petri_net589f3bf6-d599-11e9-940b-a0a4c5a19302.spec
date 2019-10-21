vars
	x0 x1 x2 x3 x4 x5 x6 x7 x8 x9 x10 x11 x12 x13 x14 x15 x16 x17 x18 x19 x20 x21 x22 x23 x24 x25 x26 x27 x28 x29 x30 x31 x32 x33 x34 x35 x36 x37 x38 x39 x40 x41 x42 x43 x44 

rules
	x8 >= 1 , x17 >= 1 ->
		x8' = x8-1,
		x28' = x28+2,
		x29' = x29+1,
		x34' = x34+1,
		x39' = x39+1,
		x42' = x42+1;

	x3 >= 1 , x16 >= 1 , x23 >= 1 , x42 >= 1 ->
		x3' = x3-1,
		x7' = x7+1,
		x16' = x16-1,
		x23' = x23-1,
		x30' = x30+1,
		x44' = x44+1;

	x0 >= 1 ->
		x0' = x0-1,
		x15' = x15+1,
		x23' = x23+1,
		x32' = x32+1;

	x23 >= 1 , x32 >= 1 , x40 >= 1 , x41 >= 2 , x43 >= 1 ->
		x8' = x8+1,
		x13' = x13+1,
		x17' = x17+1,
		x22' = x22+2,
		x23' = x23-1,
		x27' = x27+1,
		x40' = x40-1,
		x41' = x41-2;

	x4 >= 1 , x8 >= 1 , x11 >= 1 , x23 >= 1 ->
		x4' = x4-1,
		x8' = x8-1,
		x11' = x11-1,
		x13' = x13+1,
		x19' = x19+1,
		x23' = x23-1,
		x27' = x27+1;

	x6 >= 1 , x19 >= 2 ->
		x11' = x11+2,
		x12' = x12+1,
		x17' = x17+1,
		x19' = x19-2,
		x32' = x32+1,
		x34' = x34+1,
		x36' = x36+1,
		x37' = x37+1;

	x6 >= 1 , x16 >= 1 ->
		x0' = x0+1,
		x6' = x6-1,
		x8' = x8+1,
		x16' = x16-1,
		x18' = x18+1,
		x19' = x19+1,
		x22' = x22+1;

	x0 >= 1 , x1 >= 1 , x8 >= 1 , x11 >= 1 , x13 >= 1 , x35 >= 2 , x43 >= 1 ->
		x0' = x0-1,
		x1' = x1-1,
		x8' = x8-1,
		x11' = x11-1,
		x13' = x13-1,
		x18' = x18+1,
		x29' = x29+1,
		x35' = x35-2,
		x43' = x43-1;

	x4 >= 1 , x10 >= 1 , x11 >= 1 , x34 >= 1 , x42 >= 2 ->
		x2' = x2+1,
		x3' = x3+1,
		x4' = x4-1,
		x8' = x8+1,
		x10' = x10-1,
		x11' = x11-1,
		x13' = x13+1,
		x24' = x24+1,
		x34' = x34-1,
		x35' = x35+1,
		x42' = x42-2,
		x44' = x44+1;

	x5 >= 1 , x43 >= 1 ->
		x1' = x1+1,
		x3' = x3+1,
		x5' = x5-1,
		x15' = x15+1,
		x16' = x16+3,
		x21' = x21+1,
		x22' = x22+1,
		x25' = x25+1,
		x27' = x27+1,
		x43' = x43-1;

	x7 >= 1 , x9 >= 1 , x19 >= 2 , x29 >= 1 , x44 >= 2 ->
		x0' = x0+1,
		x7' = x7-1,
		x15' = x15+1,
		x19' = x19-2,
		x25' = x25+1,
		x29' = x29-1,
		x30' = x30+1,
		x34' = x34+1,
		x44' = x44-2;

	x11 >= 1 , x13 >= 1 , x15 >= 1 , x16 >= 2 , x21 >= 1 , x27 >= 1 , x35 >= 1 ->
		x3' = x3+1,
		x11' = x11-1,
		x13' = x13-1,
		x15' = x15-1,
		x16' = x16-2,
		x17' = x17+1,
		x21' = x21-1,
		x22' = x22+1,
		x26' = x26+2,
		x27' = x27-1,
		x32' = x32+1,
		x35' = x35-1,
		x40' = x40+1;

	x13 >= 1 , x15 >= 1 , x18 >= 2 ->
		x3' = x3+1,
		x9' = x9+1,
		x13' = x13-1,
		x15' = x15-1,
		x18' = x18-2,
		x21' = x21+1,
		x27' = x27+1,
		x37' = x37+1;

	x4 >= 1 , x6 >= 1 , x12 >= 2 , x21 >= 1 , x22 >= 2 , x25 >= 1 ->
		x4' = x4+1,
		x6' = x6-1,
		x12' = x12-2,
		x14' = x14+1,
		x18' = x18+1,
		x21' = x21-1,
		x22' = x22-2,
		x25' = x25-1,
		x33' = x33+1,
		x35' = x35+1,
		x41' = x41+1,
		x42' = x42+1;

	x5 >= 1 , x10 >= 1 , x12 >= 1 , x13 >= 1 , x35 >= 1 , x37 >= 1 , x38 >= 1 ->
		x5' = x5-1,
		x10' = x10-1,
		x12' = x12-1,
		x13' = x13-1,
		x17' = x17+2,
		x18' = x18+1,
		x23' = x23+1,
		x27' = x27+1,
		x37' = x37-1,
		x38' = x38-1,
		x40' = x40+1,
		x42' = x42+1;

	x17 >= 1 , x40 >= 1 ->
		x17' = x17-1,
		x21' = x21+1,
		x40' = x40-1;

	x2 >= 1 ->
		x2' = x2-1,
		x14' = x14+1;

	x26 >= 1 , x32 >= 1 ->
		x20' = x20+1,
		x26' = x26-1,
		x32' = x32-1,
		x33' = x33+1,
		x36' = x36+2;

	x5 >= 1 , x31 >= 1 , x42 >= 1 ->
		x5' = x5-1,
		x31' = x31-1,
		x33' = x33+1,
		x37' = x37+1,
		x41' = x41+1,
		x42' = x42-1;

	x4 >= 1 , x6 >= 1 , x21 >= 1 ->
		x6' = x6-1,
		x11' = x11+1,
		x20' = x20+1,
		x21' = x21-1,
		x41' = x41+1;

	x7 >= 1 , x10 >= 1 , x12 >= 1 , x24 >= 1 , x29 >= 1 , x30 >= 1 , x35 >= 1 , x39 >= 1 ->
		x10' = x10-1,
		x12' = x12-1,
		x16' = x16+2,
		x23' = x23+1,
		x24' = x24-1,
		x25' = x25+1,
		x30' = x30-1,
		x31' = x31+1,
		x35' = x35-1,
		x39' = x39-1;

	x0 >= 1 , x3 >= 1 , x9 >= 1 , x26 >= 1 , x29 >= 1 , x31 >= 2 , x32 >= 1 ->
		x0' = x0-1,
		x3' = x3-1,
		x4' = x4+1,
		x9' = x9-1,
		x13' = x13+1,
		x24' = x24+1,
		x27' = x27+1,
		x29' = x29-1,
		x31' = x31-2,
		x32' = x32-1,
		x39' = x39+1,
		x41' = x41+2;

	x7 >= 1 , x13 >= 1 , x15 >= 1 , x40 >= 1 ->
		x7' = x7-1,
		x13' = x13-1,
		x15' = x15-1,
		x22' = x22+1,
		x30' = x30+1,
		x31' = x31+1,
		x40' = x40-1,
		x42' = x42+1;

	x4 >= 1 , x36 >= 1 ->
		x4' = x4-1,
		x36' = x36-1,
		x40' = x40+1;

	x21 >= 1 , x36 >= 1 , x44 >= 1 ->
		x1' = x1+1,
		x9' = x9+1,
		x21' = x21-1,
		x34' = x34+1,
		x36' = x36-1,
		x44' = x44-1;

	x23 >= 2 ->
		x6' = x6+1,
		x11' = x11+1,
		x16' = x16+1,
		x21' = x21+2,
		x22' = x22+1,
		x23' = x23-2,
		x27' = x27+1,
		x37' = x37+1;

	x1 >= 1 , x10 >= 1 , x16 >= 1 , x21 >= 1 , x23 >= 1 ->
		x1' = x1-1,
		x2' = x2+1,
		x8' = x8+1,
		x10' = x10-1,
		x16' = x16-1,
		x21' = x21-1,
		x23' = x23-1,
		x31' = x31+1,
		x39' = x39+1,
		x40' = x40+1,
		x42' = x42+1;

	x14 >= 1 , x25 >= 1 , x31 >= 2 , x38 >= 1 ->
		x7' = x7+1,
		x14' = x14-1,
		x18' = x18+1,
		x31' = x31-2,
		x34' = x34+1,
		x38' = x38-1;

	x7 >= 1 , x10 >= 1 , x16 >= 1 , x20 >= 2 , x28 >= 1 , x35 >= 1 , x42 >= 1 ->
		x7' = x7-1,
		x8' = x8+1,
		x10' = x10-1,
		x16' = x16-1,
		x17' = x17+1,
		x20' = x20-2,
		x28' = x28-1,
		x35' = x35-1,
		x41' = x41+1,
		x42' = x42-1;

	x5 >= 1 , x9 >= 1 , x19 >= 1 , x25 >= 1 ->
		x2' = x2+1,
		x5' = x5-1,
		x6' = x6+1,
		x9' = x9-1,
		x14' = x14+1,
		x17' = x17+1,
		x19' = x19-1,
		x20' = x20+1,
		x25' = x25-1,
		x26' = x26+1,
		x33' = x33+1;

	x2 >= 1 , x35 >= 1 , x36 >= 1 ->
		x2' = x2-1,
		x17' = x17+1,
		x28' = x28+1,
		x35' = x35-1,
		x36' = x36-1,
		x41' = x41+1;

	x11 >= 1 , x16 >= 1 , x18 >= 1 ->
		x5' = x5+1,
		x9' = x9+1,
		x11' = x11-1,
		x18' = x18-1,
		x29' = x29+1,
		x33' = x33+1;

	x4 >= 1 , x5 >= 2 ->
		x4' = x4-1,
		x5' = x5-2,
		x11' = x11+2,
		x13' = x13+2,
		x16' = x16+1,
		x22' = x22+1,
		x24' = x24+1,
		x28' = x28+1,
		x40' = x40+1;

	x0 >= 1 , x19 >= 1 , x20 >= 1 , x22 >= 1 , x39 >= 1 ->
		x0' = x0-1,
		x19' = x19-1,
		x20' = x20-1,
		x22' = x22-1,
		x35' = x35+1,
		x39' = x39-1,
		x43' = x43+1;

	x14 >= 1 ->
		x14' = x14-1,
		x17' = x17+1;

	x1 >= 1 , x16 >= 1 , x17 >= 1 , x29 >= 1 , x31 >= 1 , x33 >= 1 , x36 >= 2 ->
		x0' = x0+1,
		x1' = x1-1,
		x16' = x16-1,
		x17' = x17-1,
		x29' = x29-1,
		x31' = x31-1,
		x33' = x33-1,
		x36' = x36-2;

	x6 >= 1 , x9 >= 1 , x11 >= 1 , x20 >= 1 , x29 >= 1 ->
		x9' = x9-1,
		x11' = x11-1,
		x12' = x12+1,
		x20' = x20-1,
		x24' = x24+1,
		x25' = x25+1,
		x29' = x29-1;

	x2 >= 1 , x4 >= 1 , x6 >= 1 , x28 >= 1 ->
		x0' = x0+1,
		x2' = x2-1,
		x4' = x4-1,
		x6' = x6-1,
		x9' = x9+1,
		x28' = x28-1,
		x33' = x33+1;

	x29 >= 1 , x34 >= 1 ->
		x8' = x8+1,
		x15' = x15+1,
		x24' = x24+1,
		x29' = x29-1,
		x34' = x34-1;

	x8 >= 1 , x9 >= 1 , x12 >= 1 , x28 >= 1 , x35 >= 2 ->
		x8' = x8-1,
		x9' = x9-1,
		x12' = x12-1,
		x13' = x13+1,
		x28' = x28-1,
		x32' = x32+1,
		x35' = x35-2;

	x12 >= 1 , x19 >= 1 , x31 >= 1 , x43 >= 1 ->
		x6' = x6+1,
		x7' = x7+1,
		x9' = x9+1,
		x12' = x12-1,
		x19' = x19-1,
		x21' = x21+1,
		x27' = x27+2,
		x29' = x29+2,
		x43' = x43-1;

	x20 >= 1 , x26 >= 1 , x38 >= 1 , x42 >= 1 ->
		x11' = x11+1,
		x20' = x20-1,
		x26' = x26-1,
		x38' = x38-1,
		x42' = x42-1;

	x8 >= 1 , x20 >= 1 ->
		x9' = x9+1,
		x10' = x10+1,
		x20' = x20-1,
		x44' = x44+1;

	x9 >= 1 , x11 >= 1 , x34 >= 1 , x40 >= 1 ->
		x1' = x1+1,
		x9' = x9-1,
		x11' = x11-1,
		x25' = x25+2,
		x28' = x28+1,
		x37' = x37+1,
		x42' = x42+2;

	x1 >= 1 , x3 >= 1 , x4 >= 1 , x6 >= 1 , x20 >= 1 , x21 >= 1 , x28 >= 1 , x41 >= 1 ->
		x1' = x1-1,
		x3' = x3-1,
		x4' = x4-1,
		x15' = x15+2,
		x20' = x20-1,
		x21' = x21-1,
		x28' = x28-1,
		x30' = x30+1,
		x35' = x35+1,
		x41' = x41-1;

init
	x0 = 0 , x1 = 0 , x2 = 1 , x3 = 1 , x4 = 0 , x5 = 1 , x6 = 1 , x7 = 2 , x8 = 0 , x9 = 0 , x10 = 1 , x11 = 0 , x12 = 0 , x13 = 0 , x14 = 0 , x15 = 0 , x16 = 1 , x17 = 0 , x18 = 0 , x19 = 0 , x20 = 2 , x21 = 0 , x22 = 0 , x23 = 0 , x24 = 1 , x25 = 1 , x26 = 0 , x27 = 0 , x28 = 0 , x29 = 2 , x30 = 1 , x31 = 0 , x32 = 1 , x33 = 0 , x34 = 2 , x35 = 0 , x36 = 0 , x37 = 0 , x38 = 1 , x39 = 1 , x40 = 0 , x41 = 0 , x42 = 0 , x43 = 0 , x44 = 0