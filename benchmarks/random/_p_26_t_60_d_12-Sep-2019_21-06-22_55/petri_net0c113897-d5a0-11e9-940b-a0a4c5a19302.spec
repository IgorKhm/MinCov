vars
	x0 x1 x2 x3 x4 x5 x6 x7 x8 x9 x10 x11 x12 x13 x14 x15 x16 x17 x18 x19 x20 x21 x22 x23 x24 x25 

rules
	x3 >= 1 , x4 >= 1 , x5 >= 1 , x6 >= 1 , x14 >= 1 , x16 >= 1 , x19 >= 1 ->
		x1' = x1+1,
		x3' = x3-1,
		x4' = x4-1,
		x5' = x5-1,
		x6' = x6-1,
		x8' = x8+2,
		x9' = x9+1,
		x12' = x12+3,
		x14' = x14-1,
		x15' = x15+2,
		x16' = x16-1,
		x19' = x19-1,
		x24' = x24+1;

	x2 >= 1 , x7 >= 1 , x24 >= 1 ->
		x3' = x3+1,
		x7' = x7-1,
		x19' = x19+1,
		x21' = x21+1,
		x22' = x22+1,
		x24' = x24-1;

	x8 >= 1 , x18 >= 1 , x20 >= 1 , x24 >= 1 ->
		x5' = x5+1,
		x10' = x10+2,
		x20' = x20-1,
		x23' = x23+1,
		x24' = x24-1,
		x25' = x25+1;

	x0 >= 1 , x4 >= 1 , x9 >= 1 , x10 >= 1 , x16 >= 1 , x18 >= 1 ->
		x0' = x0-1,
		x4' = x4-1,
		x9' = x9-1,
		x10' = x10-1,
		x12' = x12+1,
		x16' = x16-1,
		x18' = x18-1,
		x20' = x20+1,
		x21' = x21+1;

	x0 >= 1 , x1 >= 1 , x8 >= 1 , x16 >= 2 ->
		x0' = x0-1,
		x1' = x1-1,
		x11' = x11+1,
		x15' = x15+1,
		x16' = x16-2,
		x18' = x18+1,
		x21' = x21+1,
		x25' = x25+1;

	x17 >= 1 , x19 >= 1 ->
		x17' = x17-1,
		x18' = x18+1,
		x19' = x19-1,
		x25' = x25+1;

	x0 >= 1 , x18 >= 1 ->
		x11' = x11+1,
		x18' = x18-1,
		x21' = x21+1,
		x23' = x23+1,
		x25' = x25+1;

	x11 >= 2 , x24 >= 2 ->
		x3' = x3+1,
		x4' = x4+1,
		x6' = x6+1,
		x8' = x8+2,
		x11' = x11-2,
		x12' = x12+1,
		x16' = x16+1,
		x24' = x24-2;

	x0 >= 1 , x6 >= 1 , x20 >= 2 , x23 >= 1 , x25 >= 1 ->
		x0' = x0-1,
		x6' = x6-1,
		x10' = x10+1,
		x19' = x19+1,
		x20' = x20-1,
		x21' = x21+1,
		x23' = x23-1,
		x25' = x25-1;

	x4 >= 1 , x8 >= 1 , x15 >= 1 ->
		x1' = x1+1,
		x4' = x4-1,
		x8' = x8-1,
		x14' = x14+2,
		x15' = x15-1,
		x23' = x23+1;

	x3 >= 1 , x9 >= 1 ->
		x3' = x3-1,
		x9' = x9-1,
		x13' = x13+1,
		x14' = x14+1;

	x12 >= 1 , x16 >= 1 ->
		x1' = x1+1,
		x3' = x3+1,
		x12' = x12-1,
		x13' = x13+1,
		x14' = x14+1,
		x16' = x16-1,
		x20' = x20+1,
		x22' = x22+1,
		x25' = x25+3;

	x0 >= 1 , x1 >= 1 , x5 >= 1 , x17 >= 1 , x21 >= 1 ->
		x0' = x0-1,
		x1' = x1-1,
		x5' = x5-1,
		x14' = x14+1,
		x15' = x15+1,
		x17' = x17-1;

	x14 >= 1 ->
		x14' = x14-1,
		x25' = x25+1;

	x9 >= 1 , x15 >= 1 ->
		x0' = x0+2,
		x8' = x8+1,
		x9' = x9-1,
		x17' = x17+1,
		x20' = x20+2,
		x21' = x21+1;

	x1 >= 1 , x15 >= 1 , x19 >= 1 , x25 >= 1 ->
		x3' = x3+1,
		x9' = x9+1,
		x15' = x15-1,
		x24' = x24+1,
		x25' = x25-1;

	x4 >= 1 ->
		x4' = x4-1,
		x8' = x8+1,
		x10' = x10+1,
		x20' = x20+1,
		x21' = x21+1;

	x0 >= 1 , x12 >= 1 ->
		x0' = x0-1,
		x5' = x5+1,
		x11' = x11+1,
		x12' = x12-1;

	x3 >= 1 , x4 >= 1 , x11 >= 1 , x12 >= 1 , x17 >= 1 , x18 >= 1 , x19 >= 1 , x21 >= 1 , x24 >= 1 ->
		x2' = x2+1,
		x3' = x3-1,
		x4' = x4-1,
		x11' = x11-1,
		x12' = x12-1,
		x16' = x16+1,
		x17' = x17-1,
		x18' = x18-1,
		x19' = x19-1,
		x21' = x21-1,
		x22' = x22+1,
		x23' = x23+1,
		x24' = x24-1;

	x8 >= 1 , x11 >= 1 , x19 >= 1 , x24 >= 1 ->
		x1' = x1+1,
		x11' = x11-1,
		x16' = x16+1,
		x19' = x19-1,
		x24' = x24-1,
		x25' = x25+3;

	x15 >= 1 ->
		x11' = x11+1,
		x15' = x15-1;

	x10 >= 1 , x22 >= 1 , x23 >= 1 , x24 >= 1 , x25 >= 2 ->
		x1' = x1+1,
		x2' = x2+1,
		x3' = x3+1,
		x8' = x8+1,
		x13' = x13+1,
		x22' = x22-1,
		x23' = x23-1,
		x24' = x24-1,
		x25' = x25-2;

	x5 >= 1 , x20 >= 1 ->
		x6' = x6+1,
		x13' = x13+2,
		x17' = x17+1,
		x18' = x18+1,
		x22' = x22+1;

	x10 >= 1 , x15 >= 2 , x16 >= 1 , x18 >= 2 , x20 >= 3 ->
		x1' = x1+1,
		x10' = x10-1,
		x11' = x11+1,
		x12' = x12+2,
		x15' = x15-1,
		x16' = x16-1,
		x18' = x18-2,
		x19' = x19+1,
		x20' = x20-3,
		x22' = x22+1;

	x4 >= 1 , x5 >= 1 , x19 >= 1 , x23 >= 1 ->
		x4' = x4-1,
		x5' = x5-1,
		x15' = x15+1,
		x16' = x16+1,
		x19' = x19-1,
		x23' = x23-1;

	x2 >= 1 , x9 >= 1 , x19 >= 1 ->
		x2' = x2-1,
		x4' = x4+1,
		x6' = x6+1,
		x8' = x8+2,
		x9' = x9-1,
		x11' = x11+2,
		x14' = x14+1,
		x19' = x19-1,
		x22' = x22+1;

	x0 >= 1 , x5 >= 2 , x18 >= 1 ->
		x0' = x0-1,
		x5' = x5-2,
		x8' = x8+1,
		x14' = x14+1,
		x18' = x18-1,
		x20' = x20+1;

	x7 >= 2 , x19 >= 1 , x25 >= 2 ->
		x1' = x1+1,
		x7' = x7-2,
		x13' = x13+1,
		x14' = x14+1,
		x16' = x16+1,
		x18' = x18+1,
		x19' = x19-1,
		x25' = x25-1;

	x18 >= 1 , x21 >= 1 ->
		x8' = x8+2,
		x11' = x11+1,
		x18' = x18-1;

	x9 >= 1 , x10 >= 1 , x15 >= 1 , x19 >= 1 , x24 >= 1 ->
		x9' = x9-1,
		x10' = x10-1,
		x15' = x15-1,
		x18' = x18+1,
		x19' = x19-1,
		x22' = x22+1,
		x24' = x24-1;

	x14 >= 1 ->
		x4' = x4+2,
		x7' = x7+1,
		x8' = x8+1,
		x10' = x10+1,
		x13' = x13+1,
		x14' = x14-1,
		x15' = x15+1;

	x0 >= 1 , x7 >= 1 , x9 >= 1 , x11 >= 1 , x24 >= 1 ->
		x0' = x0-1,
		x4' = x4+1,
		x6' = x6+1,
		x7' = x7-1,
		x9' = x9-1,
		x14' = x14+1,
		x24' = x24-1;

	x1 >= 1 , x8 >= 1 , x9 >= 1 , x13 >= 2 , x14 >= 1 , x18 >= 1 ->
		x1' = x1-1,
		x8' = x8-1,
		x9' = x9-1,
		x13' = x13-2,
		x14' = x14-1,
		x17' = x17+1,
		x18' = x18-1;

	x0 >= 1 , x6 >= 1 , x17 >= 1 , x22 >= 1 ->
		x0' = x0-1,
		x2' = x2+1,
		x6' = x6-1,
		x12' = x12+1,
		x16' = x16+1,
		x17' = x17-1,
		x20' = x20+1,
		x21' = x21+1,
		x22' = x22-1,
		x24' = x24+1,
		x25' = x25+2;

	x3 >= 2 , x7 >= 1 , x14 >= 1 , x19 >= 1 , x24 >= 1 ->
		x3' = x3-2,
		x7' = x7-1,
		x13' = x13+1,
		x14' = x14-1,
		x19' = x19-1,
		x24' = x24-1;

	x0 >= 1 , x8 >= 1 , x12 >= 1 , x21 >= 1 ->
		x0' = x0-1,
		x10' = x10+1,
		x14' = x14+1,
		x15' = x15+2,
		x21' = x21-1;

	x2 >= 1 , x8 >= 1 , x9 >= 1 , x16 >= 1 , x17 >= 1 , x23 >= 1 ->
		x2' = x2-1,
		x5' = x5+1,
		x8' = x8-1,
		x9' = x9-1,
		x11' = x11+1,
		x16' = x16-1,
		x17' = x17-1,
		x23' = x23-1;

	x1 >= 1 , x9 >= 1 ->
		x1' = x1-1,
		x9' = x9-1,
		x12' = x12+2,
		x16' = x16+1,
		x17' = x17+1,
		x19' = x19+1,
		x23' = x23+1,
		x24' = x24+1,
		x25' = x25+1;

	x2 >= 1 , x5 >= 1 , x7 >= 2 , x8 >= 2 , x11 >= 1 , x15 >= 1 , x19 >= 1 ->
		x0' = x0+2,
		x2' = x2-1,
		x5' = x5-1,
		x7' = x7-2,
		x8' = x8-2,
		x9' = x9+1,
		x11' = x11+1,
		x12' = x12+1,
		x15' = x15-1,
		x20' = x20+1,
		x21' = x21+1;

	x10 >= 1 , x13 >= 1 , x15 >= 1 ->
		x2' = x2+4,
		x4' = x4+1,
		x9' = x9+1,
		x10' = x10-1,
		x12' = x12+1,
		x13' = x13-1,
		x15' = x15+1;

	x15 >= 1 ->
		x2' = x2+1,
		x3' = x3+1,
		x10' = x10+1,
		x15' = x15-1,
		x22' = x22+1,
		x23' = x23+1;

	x0 >= 1 , x1 >= 1 , x2 >= 1 , x7 >= 1 , x16 >= 2 , x18 >= 1 ->
		x0' = x0-1,
		x1' = x1-1,
		x2' = x2-1,
		x3' = x3+1,
		x4' = x4+1,
		x7' = x7-1,
		x16' = x16-2,
		x18' = x18-1,
		x19' = x19+1;

	x0 >= 1 , x1 >= 1 , x5 >= 1 , x8 >= 2 , x14 >= 1 , x16 >= 1 , x19 >= 1 ->
		x1' = x1-1,
		x2' = x2+1,
		x6' = x6+1,
		x8' = x8-2,
		x9' = x9+2,
		x11' = x11+1,
		x14' = x14-1,
		x16' = x16-1,
		x19' = x19-1,
		x22' = x22+1;

	x2 >= 1 , x8 >= 1 , x10 >= 1 , x18 >= 1 , x24 >= 1 ->
		x2' = x2-1,
		x3' = x3+1,
		x7' = x7+1,
		x8' = x8-1,
		x9' = x9+1,
		x10' = x10-1,
		x18' = x18-1,
		x19' = x19+1,
		x24' = x24-1;

	x0 >= 1 , x1 >= 1 , x3 >= 1 , x6 >= 1 , x10 >= 1 , x11 >= 1 , x12 >= 2 , x16 >= 1 , x22 >= 1 ->
		x3' = x3-1,
		x4' = x4+1,
		x6' = x6-1,
		x10' = x10-1,
		x11' = x11-1,
		x12' = x12-1,
		x16' = x16-1,
		x22' = x22-1;

	x17 >= 1 , x23 >= 1 , x24 >= 1 , x25 >= 1 ->
		x1' = x1+1,
		x2' = x2+2,
		x6' = x6+1,
		x14' = x14+1,
		x17' = x17-1,
		x18' = x18+1,
		x24' = x24-1,
		x25' = x25-1;

	x3 >= 1 , x20 >= 1 , x25 >= 1 ->
		x2' = x2+1,
		x3' = x3-1,
		x7' = x7+2,
		x9' = x9+1,
		x10' = x10+1,
		x12' = x12+1,
		x15' = x15+1,
		x20' = x20-1,
		x22' = x22+1,
		x25' = x25-1;

	x0 >= 1 , x1 >= 1 , x3 >= 1 , x9 >= 1 , x25 >= 1 ->
		x0' = x0-1,
		x1' = x1-1,
		x3' = x3-1,
		x9' = x9-1,
		x11' = x11+1,
		x13' = x13+1,
		x14' = x14+1,
		x15' = x15+1,
		x20' = x20+1,
		x22' = x22+1,
		x25' = x25-1;

	x21 >= 1 , x25 >= 1 ->
		x3' = x3+1,
		x6' = x6+1,
		x9' = x9+1,
		x10' = x10+2,
		x11' = x11+1,
		x14' = x14+1,
		x17' = x17+1,
		x21' = x21-1,
		x23' = x23+1,
		x25' = x25-1;

	x9 >= 1 , x16 >= 2 ->
		x0' = x0+1,
		x7' = x7+1,
		x9' = x9-1,
		x10' = x10+1,
		x12' = x12+1,
		x15' = x15+1,
		x16' = x16-2;

	x8 >= 1 , x13 >= 1 , x19 >= 1 , x23 >= 1 , x24 >= 1 ->
		x1' = x1+1,
		x7' = x7+1,
		x8' = x8-1,
		x9' = x9+1,
		x10' = x10+1,
		x12' = x12+1,
		x19' = x19-1;

	x7 >= 1 , x13 >= 1 , x14 >= 1 , x16 >= 1 , x20 >= 1 , x23 >= 1 , x25 >= 1 ->
		x7' = x7-1,
		x8' = x8+1,
		x13' = x13-1,
		x14' = x14-1,
		x16' = x16-1,
		x20' = x20-1,
		x23' = x23-1,
		x24' = x24+1,
		x25' = x25-1;

	x0 >= 1 , x2 >= 2 , x7 >= 1 , x8 >= 1 , x10 >= 2 , x15 >= 1 , x18 >= 1 ->
		x0' = x0-1,
		x1' = x1+1,
		x2' = x2-2,
		x3' = x3+2,
		x5' = x5+1,
		x8' = x8-1,
		x9' = x9+1,
		x10' = x10-2,
		x15' = x15-1,
		x18' = x18-1;

	x19 >= 1 ->
		x7' = x7+1,
		x19' = x19-1;

	x10 >= 1 , x12 >= 1 , x13 >= 1 ->
		x2' = x2+1,
		x6' = x6+1,
		x12' = x12-1;

	x4 >= 1 , x23 >= 1 ->
		x1' = x1+2,
		x4' = x4-1,
		x23' = x23-1;

	x8 >= 1 , x11 >= 1 , x15 >= 1 , x20 >= 1 ->
		x6' = x6+1,
		x8' = x8-1,
		x9' = x9+1,
		x11' = x11-1,
		x15' = x15+1,
		x20' = x20-1;

	x13 >= 1 , x18 >= 1 ->
		x0' = x0+1,
		x3' = x3+1,
		x8' = x8+1,
		x13' = x13-1,
		x14' = x14+1,
		x18' = x18-1,
		x19' = x19+1,
		x23' = x23+2;

	x4 >= 1 , x5 >= 1 , x15 >= 2 , x18 >= 1 , x23 >= 1 , x24 >= 1 ->
		x4' = x4-1,
		x5' = x5-1,
		x15' = x15-2,
		x17' = x17+1,
		x19' = x19+1,
		x20' = x20+1,
		x22' = x22+1,
		x23' = x23-1,
		x24' = x24-1;

	x4 >= 1 , x5 >= 1 , x10 >= 1 , x20 >= 1 , x21 >= 1 , x23 >= 1 ->
		x4' = x4-1,
		x7' = x7+1,
		x10' = x10-1,
		x14' = x14+1,
		x16' = x16+1,
		x20' = x20-1,
		x21' = x21-1;

init
	x0 = 0 , x1 = 0 , x2 = 0 , x3 = 0 , x4 = 0 , x5 = 0 , x6 = 1 , x7 = 0 , x8 = 0 , x9 = 0 , x10 = 0 , x11 = 1 , x12 = 1 , x13 = 0 , x14 = 1 , x15 = 1 , x16 = 2 , x17 = 0 , x18 = 0 , x19 = 1 , x20 = 1 , x21 = 0 , x22 = 0 , x23 = 0 , x24 = 1 , x25 = 0