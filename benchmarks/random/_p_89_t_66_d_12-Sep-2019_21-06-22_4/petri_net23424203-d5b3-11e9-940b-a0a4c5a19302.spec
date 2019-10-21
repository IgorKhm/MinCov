vars
	x0 x1 x2 x3 x4 x5 x6 x7 x8 x9 x10 x11 x12 x13 x14 x15 x16 x17 x18 x19 x20 x21 x22 x23 x24 x25 x26 x27 x28 x29 x30 x31 x32 x33 x34 x35 x36 x37 x38 x39 x40 x41 x42 x43 x44 x45 x46 x47 x48 x49 x50 x51 x52 x53 x54 x55 x56 x57 x58 x59 x60 x61 x62 x63 x64 x65 x66 x67 x68 x69 x70 x71 x72 x73 x74 x75 x76 x77 x78 x79 x80 x81 x82 x83 x84 x85 x86 x87 x88 

rules
	x27 >= 1 , x36 >= 1 , x50 >= 1 , x72 >= 1 , x75 >= 1 ->
		x6' = x6+1,
		x27' = x27-1,
		x36' = x36-1,
		x39' = x39+1,
		x40' = x40+1,
		x50' = x50-1,
		x68' = x68+1,
		x72' = x72-1,
		x75' = x75-1;

	x3 >= 1 , x12 >= 1 , x15 >= 1 , x30 >= 1 , x39 >= 1 , x42 >= 1 , x44 >= 1 , x66 >= 1 ->
		x3' = x3-1,
		x12' = x12-1,
		x15' = x15-1,
		x27' = x27+1,
		x30' = x30-1,
		x39' = x39-1,
		x42' = x42-1,
		x44' = x44-1,
		x52' = x52+1,
		x54' = x54+1,
		x66' = x66-1,
		x67' = x67+1;

	x2 >= 1 , x7 >= 1 , x11 >= 1 , x30 >= 1 , x36 >= 1 , x58 >= 1 , x77 >= 1 , x82 >= 1 ->
		x1' = x1+1,
		x2' = x2-1,
		x7' = x7-1,
		x11' = x11-1,
		x24' = x24+1,
		x30' = x30-1,
		x36' = x36-1,
		x44' = x44+1,
		x49' = x49+1,
		x53' = x53+1,
		x58' = x58-1,
		x67' = x67+1,
		x77' = x77-1,
		x80' = x80+1,
		x82' = x82-1;

	x15 >= 1 , x28 >= 1 , x40 >= 1 , x65 >= 1 , x66 >= 1 , x68 >= 1 , x73 >= 1 , x81 >= 1 ->
		x2' = x2+1,
		x13' = x13+1,
		x15' = x15-1,
		x28' = x28-1,
		x38' = x38+1,
		x40' = x40-1,
		x44' = x44+1,
		x48' = x48+1,
		x53' = x53+1,
		x57' = x57+1,
		x65' = x65-1,
		x66' = x66-1,
		x68' = x68-1,
		x73' = x73-1,
		x77' = x77+1,
		x81' = x81-1;

	x3 >= 1 , x14 >= 1 , x17 >= 1 , x19 >= 1 , x23 >= 1 , x63 >= 1 , x86 >= 1 ->
		x3' = x3-1,
		x4' = x4+2,
		x14' = x14-1,
		x15' = x15+1,
		x17' = x17-1,
		x19' = x19-1,
		x23' = x23-1,
		x35' = x35+1,
		x37' = x37+1,
		x63' = x63-1,
		x64' = x64+1,
		x79' = x79+1,
		x86' = x86-1,
		x88' = x88+1;

	x7 >= 1 , x31 >= 1 , x35 >= 1 , x41 >= 1 , x42 >= 1 , x81 >= 1 , x84 >= 1 , x87 >= 1 ->
		x1' = x1+1,
		x4' = x4+1,
		x7' = x7-1,
		x18' = x18+1,
		x21' = x21+1,
		x31' = x31-1,
		x35' = x35-1,
		x41' = x41-1,
		x42' = x42-1,
		x70' = x70+1,
		x79' = x79+1,
		x81' = x81-1,
		x84' = x84-1,
		x87' = x87-1;

	x12 >= 1 , x13 >= 1 , x20 >= 1 , x25 >= 1 , x26 >= 1 , x44 >= 1 , x55 >= 1 ->
		x12' = x12-1,
		x13' = x13-1,
		x18' = x18+1,
		x20' = x20-1,
		x25' = x25-1,
		x26' = x26-1,
		x44' = x44-1,
		x55' = x55-1,
		x87' = x87+1;

	x1 >= 1 , x11 >= 1 , x17 >= 1 , x72 >= 1 , x76 >= 1 ->
		x11' = x11-1,
		x14' = x14+1,
		x17' = x17-1,
		x45' = x45+1,
		x72' = x72-1,
		x76' = x76-1;

	x5 >= 1 , x6 >= 1 , x29 >= 1 , x34 >= 1 , x60 >= 2 , x69 >= 1 ->
		x2' = x2+1,
		x5' = x5-1,
		x6' = x6-1,
		x11' = x11+1,
		x29' = x29-1,
		x34' = x34-1,
		x40' = x40+1,
		x44' = x44+1,
		x60' = x60-2,
		x69' = x69-1,
		x76' = x76+1;

	x9 >= 1 , x14 >= 1 , x36 >= 1 , x55 >= 1 , x61 >= 1 , x74 >= 1 , x82 >= 1 ->
		x5' = x5+1,
		x9' = x9-1,
		x13' = x13+1,
		x14' = x14-1,
		x23' = x23+1,
		x36' = x36-1,
		x38' = x38+1,
		x57' = x57+1,
		x59' = x59+1,
		x61' = x61-1,
		x70' = x70+1,
		x74' = x74-1,
		x82' = x82-1;

	x14 >= 1 , x17 >= 1 , x36 >= 3 , x39 >= 1 , x53 >= 1 , x63 >= 1 , x64 >= 1 ->
		x1' = x1+1,
		x15' = x15+1,
		x17' = x17-1,
		x25' = x25+1,
		x36' = x36-3,
		x39' = x39-1,
		x40' = x40+1,
		x44' = x44+1,
		x53' = x53-1,
		x63' = x63-1,
		x64' = x64-1,
		x68' = x68+1,
		x85' = x85+1;

	x10 >= 1 , x11 >= 1 , x74 >= 1 , x75 >= 2 ->
		x10' = x10-1,
		x11' = x11-1,
		x28' = x28+1,
		x63' = x63+2,
		x74' = x74-1,
		x75' = x75-2;

	x17 >= 1 , x18 >= 1 , x22 >= 1 , x23 >= 1 , x29 >= 1 , x38 >= 1 , x71 >= 1 ->
		x11' = x11+1,
		x12' = x12+1,
		x17' = x17-1,
		x18' = x18-1,
		x20' = x20+1,
		x22' = x22-1,
		x23' = x23-1,
		x29' = x29-1,
		x38' = x38-1,
		x41' = x41+1,
		x56' = x56+1,
		x70' = x70+1,
		x71' = x71-1,
		x81' = x81+1,
		x82' = x82+1;

	x24 >= 1 , x36 >= 1 , x88 >= 1 ->
		x0' = x0+1,
		x24' = x24-1,
		x31' = x31+1,
		x36' = x36-1,
		x63' = x63+1,
		x65' = x65+1,
		x88' = x88-1;

	x10 >= 1 , x30 >= 1 , x38 >= 1 , x41 >= 1 , x47 >= 1 , x74 >= 1 , x79 >= 1 ->
		x10' = x10-1,
		x16' = x16+1,
		x30' = x30-1,
		x38' = x38-1,
		x41' = x41-1,
		x47' = x47-1,
		x51' = x51+1,
		x63' = x63+2,
		x67' = x67+1,
		x74' = x74-1,
		x75' = x75+1,
		x79' = x79-1,
		x82' = x82+1;

	x43 >= 1 , x65 >= 1 , x80 >= 1 ->
		x4' = x4+1,
		x26' = x26+1,
		x31' = x31+1,
		x43' = x43-1,
		x50' = x50+1,
		x60' = x60+1,
		x61' = x61+1,
		x65' = x65-1,
		x68' = x68+1,
		x80' = x80-1;

	x19 >= 1 , x32 >= 1 , x35 >= 1 , x51 >= 1 , x77 >= 1 ->
		x7' = x7+1,
		x19' = x19-1,
		x21' = x21+1,
		x23' = x23+1,
		x32' = x32-1,
		x35' = x35-1,
		x42' = x42+1,
		x48' = x48+1,
		x51' = x51-1,
		x59' = x59+1,
		x60' = x60+1,
		x77' = x77-1;

	x42 >= 1 ->
		x8' = x8+1,
		x36' = x36+1,
		x42' = x42-1,
		x44' = x44+1,
		x47' = x47+1,
		x68' = x68+1,
		x72' = x72+1;

	x3 >= 1 , x24 >= 1 , x35 >= 1 , x37 >= 1 , x60 >= 1 , x73 >= 1 , x75 >= 1 , x80 >= 1 ->
		x3' = x3-1,
		x4' = x4+1,
		x16' = x16+1,
		x24' = x24-1,
		x25' = x25+1,
		x37' = x37-1,
		x49' = x49+1,
		x53' = x53+1,
		x60' = x60-1,
		x68' = x68+1,
		x75' = x75-1,
		x80' = x80-1,
		x87' = x87+1;

	x2 >= 1 , x22 >= 1 , x65 >= 1 , x86 >= 1 ->
		x2' = x2-1,
		x12' = x12+1,
		x29' = x29+1,
		x46' = x46+1,
		x53' = x53+1,
		x65' = x65-1,
		x82' = x82+1,
		x85' = x85+1,
		x86' = x86-1,
		x87' = x87+1;

	x7 >= 1 , x17 >= 1 , x51 >= 1 , x72 >= 1 , x77 >= 1 , x81 >= 1 ->
		x7' = x7-1,
		x8' = x8+1,
		x9' = x9+1,
		x17' = x17-1,
		x23' = x23+1,
		x51' = x51-1,
		x71' = x71+1,
		x72' = x72-1,
		x73' = x73+1,
		x77' = x77-1,
		x81' = x81-1;

	x9 >= 1 , x54 >= 1 , x70 >= 1 , x84 >= 2 ->
		x34' = x34+1,
		x54' = x54-1,
		x55' = x55+1,
		x70' = x70-1,
		x84' = x84-2;

	x73 >= 1 , x79 >= 1 ->
		x26' = x26+1,
		x69' = x69+1,
		x73' = x73-1;

	x9 >= 1 , x25 >= 1 , x41 >= 1 , x57 >= 1 , x59 >= 1 , x69 >= 1 , x77 >= 1 , x88 >= 1 ->
		x9' = x9-1,
		x18' = x18+1,
		x25' = x25-1,
		x27' = x27+1,
		x41' = x41-1,
		x44' = x44+1,
		x56' = x56+1,
		x57' = x57-1,
		x59' = x59-1,
		x62' = x62+2,
		x64' = x64+1,
		x66' = x66+1,
		x67' = x67+1,
		x69' = x69-1,
		x77' = x77-1,
		x85' = x85+1,
		x88' = x88-1;

	x77 >= 1 ->
		x71' = x71+1,
		x77' = x77-1;

	x15 >= 1 , x19 >= 1 , x67 >= 1 , x79 >= 1 , x85 >= 1 ->
		x1' = x1+1,
		x15' = x15-1,
		x19' = x19-1,
		x33' = x33+1,
		x53' = x53+1,
		x57' = x57+1,
		x63' = x63+1,
		x67' = x67-1,
		x72' = x72+1,
		x79' = x79-1,
		x85' = x85-1,
		x87' = x87+1;

	x27 >= 1 , x41 >= 1 , x65 >= 1 , x66 >= 1 ->
		x9' = x9+1,
		x17' = x17+1,
		x27' = x27-1,
		x41' = x41-1,
		x55' = x55+1,
		x65' = x65-1,
		x66' = x66-1,
		x73' = x73+1;

	x1 >= 1 , x28 >= 1 , x31 >= 1 , x47 >= 1 , x54 >= 1 , x60 >= 1 , x63 >= 1 , x72 >= 1 ->
		x1' = x1-1,
		x14' = x14+1,
		x25' = x25+1,
		x28' = x28-1,
		x31' = x31-1,
		x47' = x47-1,
		x51' = x51+1,
		x54' = x54-1,
		x55' = x55+1,
		x57' = x57+1,
		x60' = x60-1,
		x63' = x63-1,
		x68' = x68+1,
		x76' = x76+1,
		x78' = x78+1;

	x30 >= 1 , x41 >= 1 , x48 >= 1 , x53 >= 1 , x66 >= 1 ->
		x7' = x7+1,
		x30' = x30-1,
		x36' = x36+1,
		x41' = x41-1,
		x48' = x48-1,
		x53' = x53-1,
		x56' = x56+1,
		x62' = x62+1,
		x76' = x76+1,
		x83' = x83+1,
		x87' = x87+1;

	x21 >= 1 , x74 >= 1 , x88 >= 1 ->
		x1' = x1+1,
		x9' = x9+1,
		x17' = x17+1,
		x21' = x21-1,
		x27' = x27+1,
		x31' = x31+1,
		x40' = x40+1,
		x44' = x44+1,
		x45' = x45+1,
		x57' = x57+1,
		x74' = x74-1,
		x88' = x88-1;

	x4 >= 2 , x27 >= 1 ->
		x4' = x4-2,
		x6' = x6+1,
		x7' = x7+2,
		x12' = x12+1,
		x26' = x26+1,
		x27' = x27-1,
		x44' = x44+1,
		x57' = x57+1,
		x63' = x63+1;

	x72 >= 1 , x88 >= 1 ->
		x62' = x62+1,
		x72' = x72-1,
		x88' = x88-1;

	x27 >= 1 , x59 >= 1 , x66 >= 1 ->
		x5' = x5+1,
		x13' = x13+1,
		x21' = x21+1,
		x25' = x25+1,
		x27' = x27-1,
		x44' = x44+1,
		x56' = x56+1,
		x59' = x59-1,
		x66' = x66-1,
		x83' = x83+1;

	x28 >= 1 ->
		x28' = x28-1,
		x32' = x32+1,
		x33' = x33+1,
		x49' = x49+1,
		x57' = x57+1,
		x65' = x65+1;

	x27 >= 1 ->
		x27' = x27-1,
		x53' = x53+1;

	x44 >= 1 , x52 >= 1 , x53 >= 1 , x69 >= 3 , x84 >= 1 ->
		x34' = x34+1,
		x44' = x44-1,
		x47' = x47+1,
		x52' = x52-1,
		x53' = x53-1,
		x69' = x69-3,
		x84' = x84-1;

	x8 >= 1 , x55 >= 1 ->
		x8' = x8-1,
		x20' = x20+1,
		x32' = x32+1,
		x37' = x37+1,
		x55' = x55-1,
		x60' = x60+1,
		x68' = x68+1;

	x0 >= 2 , x6 >= 1 , x16 >= 1 , x40 >= 1 , x50 >= 1 , x65 >= 1 , x73 >= 1 ->
		x0' = x0-2,
		x6' = x6-1,
		x11' = x11+1,
		x16' = x16-1,
		x21' = x21+1,
		x33' = x33+1,
		x37' = x37+1,
		x40' = x40-1,
		x50' = x50-1,
		x65' = x65-1,
		x73' = x73-1,
		x78' = x78+1;

	x29 >= 1 , x42 >= 1 , x55 >= 1 , x58 >= 1 , x62 >= 1 , x63 >= 1 , x71 >= 1 , x79 >= 1 ->
		x8' = x8+1,
		x29' = x29-1,
		x42' = x42-1,
		x55' = x55-1,
		x58' = x58-1,
		x62' = x62-1,
		x63' = x63-1,
		x71' = x71-1,
		x79' = x79-1;

	x9 >= 2 , x32 >= 1 , x50 >= 1 , x61 >= 1 ->
		x9' = x9-2,
		x16' = x16+1,
		x32' = x32-1,
		x50' = x50-1,
		x61' = x61-1,
		x87' = x87+1;

	x0 >= 2 , x13 >= 1 , x40 >= 2 , x73 >= 1 ->
		x0' = x0-2,
		x13' = x13-1,
		x40' = x40-2,
		x42' = x42+1,
		x49' = x49+1,
		x73' = x73-1,
		x86' = x86+2;

	x61 >= 1 ->
		x15' = x15+1,
		x25' = x25+1,
		x26' = x26+1,
		x44' = x44+1,
		x47' = x47+1,
		x61' = x61-1,
		x65' = x65+1,
		x84' = x84+1,
		x85' = x85+2;

	x25 >= 1 ->
		x5' = x5+1,
		x7' = x7+1,
		x10' = x10+1,
		x23' = x23+1,
		x25' = x25-1,
		x47' = x47+1,
		x49' = x49+1;

	x47 >= 1 , x70 >= 1 , x77 >= 1 , x82 >= 1 ->
		x8' = x8+1,
		x15' = x15+1,
		x23' = x23+1,
		x34' = x34+1,
		x45' = x45+1,
		x47' = x47-1,
		x51' = x51+2,
		x57' = x57+1,
		x70' = x70-1,
		x77' = x77-1,
		x82' = x82-1,
		x85' = x85+1,
		x88' = x88+1;

	x0 >= 1 , x7 >= 1 , x12 >= 1 , x14 >= 1 , x21 >= 1 , x46 >= 1 , x50 >= 1 , x54 >= 1 , x85 >= 1 ->
		x0' = x0-1,
		x7' = x7-1,
		x12' = x12-1,
		x14' = x14-1,
		x21' = x21-1,
		x25' = x25+1,
		x32' = x32+1,
		x39' = x39+1,
		x40' = x40+1,
		x41' = x41+1,
		x46' = x46-1,
		x50' = x50-1,
		x54' = x54-1,
		x63' = x63+1,
		x64' = x64+1,
		x85' = x85-1;

	x9 >= 1 , x25 >= 1 , x32 >= 1 , x44 >= 1 , x48 >= 1 , x61 >= 1 , x63 >= 1 , x77 >= 1 ->
		x9' = x9-1,
		x23' = x23+1,
		x25' = x25-1,
		x32' = x32-1,
		x33' = x33+2,
		x35' = x35+1,
		x44' = x44-1,
		x48' = x48-1,
		x61' = x61-1,
		x63' = x63-1,
		x77' = x77-1;

	x8 >= 1 , x19 >= 2 , x27 >= 1 , x69 >= 1 , x76 >= 1 , x84 >= 1 ->
		x8' = x8-1,
		x19' = x19-2,
		x27' = x27-1,
		x29' = x29+1,
		x35' = x35+1,
		x40' = x40+1,
		x60' = x60+1,
		x69' = x69-1,
		x76' = x76-1,
		x79' = x79+1,
		x84' = x84-1;

	x5 >= 1 , x12 >= 1 , x15 >= 1 , x21 >= 1 , x25 >= 1 , x76 >= 1 , x85 >= 1 ->
		x12' = x12-1,
		x19' = x19+1,
		x21' = x21-1,
		x25' = x25-1,
		x27' = x27+1,
		x28' = x28+1,
		x54' = x54+1,
		x76' = x76-1,
		x85' = x85-1;

	x10 >= 1 , x12 >= 1 , x36 >= 1 , x54 >= 1 , x59 >= 1 , x84 >= 1 ->
		x10' = x10-1,
		x12' = x12-1,
		x17' = x17+1,
		x19' = x19+1,
		x36' = x36-1,
		x54' = x54-1,
		x59' = x59-1;

	x15 >= 1 , x16 >= 2 , x33 >= 1 , x39 >= 1 , x56 >= 1 , x64 >= 1 ->
		x15' = x15-1,
		x16' = x16-2,
		x32' = x32+1,
		x33' = x33-1,
		x39' = x39-1,
		x45' = x45+1,
		x64' = x64-1;

	x7 >= 1 , x84 >= 1 ->
		x7' = x7-1,
		x41' = x41+1,
		x49' = x49+1,
		x64' = x64+1,
		x84' = x84-1;

	x25 >= 1 , x38 >= 1 , x62 >= 1 , x88 >= 1 ->
		x13' = x13+1,
		x23' = x23+1,
		x25' = x25-1,
		x26' = x26+1,
		x35' = x35+1,
		x38' = x38-1,
		x59' = x59+2,
		x62' = x62-1,
		x66' = x66+1,
		x75' = x75+1,
		x82' = x82+1,
		x88' = x88-1;

	x28 >= 1 , x41 >= 1 , x49 >= 1 , x51 >= 1 , x66 >= 1 , x71 >= 1 , x76 >= 1 , x80 >= 1 ->
		x6' = x6+1,
		x17' = x17+1,
		x28' = x28-1,
		x41' = x41-1,
		x49' = x49-1,
		x51' = x51-1,
		x52' = x52+1,
		x59' = x59+1,
		x66' = x66-1,
		x71' = x71-1,
		x76' = x76-1,
		x80' = x80-1,
		x87' = x87+1;

	x27 >= 1 , x38 >= 1 , x62 >= 1 ->
		x12' = x12+1,
		x27' = x27-1,
		x38' = x38-1,
		x62' = x62-1,
		x76' = x76+1;

	x68 >= 1 ->
		x20' = x20+1,
		x62' = x62+1,
		x68' = x68-1;

	x14 >= 1 , x18 >= 1 , x59 >= 1 , x77 >= 1 , x86 >= 2 ->
		x14' = x14-1,
		x18' = x18-1,
		x23' = x23+1,
		x52' = x52+1,
		x59' = x59-1,
		x77' = x77-1,
		x86' = x86-2;

	x0 >= 1 , x3 >= 1 , x4 >= 2 , x9 >= 1 , x27 >= 1 , x43 >= 1 , x72 >= 1 ->
		x0' = x0-1,
		x3' = x3-1,
		x4' = x4-2,
		x9' = x9-1,
		x27' = x27-1,
		x41' = x41+2,
		x43' = x43-1,
		x53' = x53+1,
		x67' = x67+2,
		x70' = x70+1,
		x72' = x72-1,
		x79' = x79+1,
		x88' = x88+1;

	x26 >= 1 , x38 >= 1 , x49 >= 1 , x50 >= 1 , x53 >= 1 , x84 >= 1 ->
		x6' = x6+2,
		x17' = x17+1,
		x18' = x18+2,
		x26' = x26-1,
		x49' = x49-1,
		x50' = x50-1,
		x53' = x53-1,
		x66' = x66+1,
		x67' = x67+1,
		x84' = x84-1;

	x83 >= 1 ->
		x6' = x6+1,
		x7' = x7+2,
		x21' = x21+1,
		x27' = x27+1,
		x31' = x31+1,
		x40' = x40+1,
		x65' = x65+1,
		x83' = x83-1;

	x2 >= 1 , x8 >= 1 , x10 >= 1 , x12 >= 1 , x13 >= 1 , x17 >= 1 , x32 >= 1 , x38 >= 1 , x66 >= 1 ->
		x0' = x0+1,
		x2' = x2-1,
		x4' = x4+1,
		x8' = x8-1,
		x10' = x10-1,
		x12' = x12-1,
		x13' = x13-1,
		x17' = x17-1,
		x32' = x32-1,
		x38' = x38-1,
		x66' = x66-1,
		x78' = x78+1;

	x40 >= 1 , x87 >= 1 ->
		x32' = x32+1,
		x37' = x37+1,
		x40' = x40-1,
		x49' = x49+1,
		x73' = x73+1,
		x87' = x87-1;

	x19 >= 1 , x42 >= 1 , x66 >= 1 , x78 >= 1 , x86 >= 1 ->
		x19' = x19-1,
		x34' = x34+1,
		x42' = x42-1,
		x43' = x43+1,
		x65' = x65+1,
		x66' = x66-1,
		x71' = x71+1,
		x78' = x78-1,
		x79' = x79+1,
		x86' = x86-1;

	x0 >= 1 , x43 >= 1 , x70 >= 1 , x71 >= 1 , x87 >= 1 ->
		x0' = x0-1,
		x4' = x4+2,
		x10' = x10+1,
		x32' = x32+1,
		x36' = x36+1,
		x43' = x43-1,
		x56' = x56+1,
		x70' = x70-1,
		x71' = x71-1,
		x82' = x82+1,
		x87' = x87-1;

	x6 >= 1 , x7 >= 1 , x22 >= 1 , x32 >= 1 , x76 >= 1 , x79 >= 1 ->
		x6' = x6-1,
		x7' = x7-1,
		x22' = x22-1,
		x32' = x32-1,
		x50' = x50+1,
		x76' = x76-1,
		x79' = x79-1;

	x20 >= 1 , x61 >= 1 ->
		x20' = x20-1,
		x61' = x61-1,
		x79' = x79+1;

	x17 >= 1 ->
		x8' = x8+1,
		x11' = x11+1,
		x15' = x15+1,
		x27' = x27+1,
		x69' = x69+2,
		x70' = x70+1,
		x71' = x71+1;

init
	x0 = 0 , x1 = 0 , x2 = 0 , x3 = 1 , x4 = 0 , x5 = 0 , x6 = 0 , x7 = 2 , x8 = 1 , x9 = 0 , x10 = 0 , x11 = 0 , x12 = 1 , x13 = 1 , x14 = 0 , x15 = 0 , x16 = 0 , x17 = 1 , x18 = 0 , x19 = 1 , x20 = 0 , x21 = 0 , x22 = 2 , x23 = 0 , x24 = 0 , x25 = 0 , x26 = 0 , x27 = 0 , x28 = 0 , x29 = 0 , x30 = 0 , x31 = 0 , x32 = 1 , x33 = 0 , x34 = 0 , x35 = 1 , x36 = 1 , x37 = 0 , x38 = 0 , x39 = 1 , x40 = 0 , x41 = 0 , x42 = 0 , x43 = 0 , x44 = 0 , x45 = 0 , x46 = 0 , x47 = 0 , x48 = 0 , x49 = 0 , x50 = 0 , x51 = 0 , x52 = 1 , x53 = 0 , x54 = 0 , x55 = 1 , x56 = 1 , x57 = 0 , x58 = 1 , x59 = 1 , x60 = 0 , x61 = 1 , x62 = 1 , x63 = 1 , x64 = 0 , x65 = 0 , x66 = 1 , x67 = 1 , x68 = 0 , x69 = 0 , x70 = 0 , x71 = 0 , x72 = 1 , x73 = 1 , x74 = 0 , x75 = 1 , x76 = 1 , x77 = 0 , x78 = 0 , x79 = 0 , x80 = 0 , x81 = 1 , x82 = 0 , x83 = 1 , x84 = 0 , x85 = 1 , x86 = 0 , x87 = 1 , x88 = 0