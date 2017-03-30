% A comparison for various image denoising algorithms on the famous "lena"
% image. One example call for each denoising algorithm is included, the
% resulting images are stored. This code may serve as an example on how to
% use the various algorithms.
%
% Author: Markus Mayer, Pattern Recognition Lab, University
% of Erlangen-Nuremberg, markus.mayer@informatik.uni-erlangen.de

% Load image, store noisy version as well as original

img = double(imread('lena.jpg'));

img = img./ 255;

imgNoise = img + randn(size(img)) .* 0.2;
imgNoise(imgNoise < 0) = 0;
imgNoise(imgNoise > 1) = 1;

imwrite(img, 'lenaOrig.jpg', 'Quality', 100);
imwrite(imgNoise, 'lenaNoise.jpg', 'Quality', 100);

% Apply the denoising algorithms and store the results

imgWaveletHard = waveletHardThreshold(imgNoise, 'mu', 0.15, 'lmax', 5, 'basis', 'dddtcwt');
imwrite(imgWaveletHard, 'lenaWaveletHard.jpg', 'Quality', 100);

imgWaveletSoft = waveletSoftThreshold(imgNoise, 'mu', 0.15, 'lmax', 5, 'basis', 'dddtcwt');
imwrite(imgWaveletSoft, 'lenaWaveletSoft.jpg', 'Quality', 100);

imgComplex = diffusionPeronaMalik(imgNoise, 'function', 'complex', 'sigma', 0.02, 'time', 10 , 'maxIter', 300);
imwrite(imgComplex, 'lenaComplex.jpg', 'Quality', 100);

imgAnisotropic = diffusionAnisotropic(imgNoise, 'function', 'tuckey', 'sigma', 0.005, 'time', 2 , 'maxIter', 300);
imwrite(imgAnisotropic, 'lenaAnisotropic.jpg', 'Quality', 100);

imgBayes = bayesEstimateDenoise(imgNoise, 'sigmaSpatial', 3, 'windowSize', 3, 'sigmaFactor', 2);
imwrite(imgBayes, 'lenaBayes.jpg', 'Quality', 100);

% A special section for the multiframe method:

imgNoiseVol = zeros(size(img, 1), size(img, 2), 4);

for i = 1:4
    imgNoise = img + randn(size(img)) .* 0.2;
    imgNoise(imgNoise < 0) = 0;
    imgNoise(imgNoise > 1) = 1;

    imgNoiseVol(:,:,i) = imgNoise;
end

imgWaveletMultiframe = waveletMultiFrame(imgNoiseVol, 'k', 6, 'p', 4, 'maxLevel', 5, 'weightMode', 4, 'basis', 'dualTree');
imwrite(imgWaveletMultiframe, 'lenaMultiframe.jpg', 'Quality', 100);