% motion files
pkg load image
directory = dir('motion-img');
[n x] = size(directory);
a = im2double(imread(["motion-img/" directory(3).name] ));
[w h] = size(a);
accum = double(zeros(w,h));
for i=3:n	
	a = im2double(imread([ 'motion-img/' directory(i).name] ));
	accum = accum + a;
end

mask = accum < 0.01;

imwrite(mask, 'mask.png');
