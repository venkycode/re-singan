time python customSR.py --input_dir ./Input/customSR --input_name 11.png --noisy_input_name 24.png --sr_factor 2 --ker_size 2 --niter 1000  --lr_g 0.001 --lr_d 0.001 --custom_sr_alpha 20 --frozenWeight 0.7 --nc_im 1 --nc_z 1 --skip_training 1 --threshold 256
git add .
git commit -m "T=256, 24.png"
time python customSR.py --input_dir ./Input/customSR --input_name 11.png --noisy_input_name 50.png --sr_factor 2 --ker_size 2 --niter 1000  --lr_g 0.001 --lr_d 0.001 --custom_sr_alpha 20 --frozenWeight 0.7 --nc_im 1 --nc_z 1 --skip_training 1 --threshold 256 
git add .
git commit -m "T=256, 50.png"
#time python customSR.py --input_dir ./Input/customSR --input_name 11.png --noisy_input_name 63.png --sr_factor 2 --ker_size 2 --niter 1000  --lr_g 0.001 --lr_d 0.001 --custom_sr_alpha 20 --frozenWeight 0.7 --nc_im 1 --nc_z 1 --skip_training 0 --threshold 256 
#git add .
#git commit -m "T=256"
# time python customSR.py --input_dir ./Input/customSR --input_name 11.png --noisy_input_name 86_input.png --sr_factor 2 --ker_size 2 --niter 1000  --lr_g 0.001 --lr_d 0.001 --custom_sr_alpha 20 --frozenWeight 0.7 --nc_im 1 --nc_z 1 --skip_training 1 --threshold 128 
# git add .
# git commit -m "run3"
# time python customSR.py --input_dir ./Input/customSR --input_name 11.png --noisy_input_name 99_input.png --sr_factor 2 --ker_size 2 --niter 1000  --lr_g 0.001 --lr_d 0.001 --custom_sr_alpha 20 --frozenWeight 0.7 --nc_im 1 --nc_z 1 --skip_training 1 --threshold 128 
# git add .
# git commit -m "run4"
# time python customSR.py --input_dir ./Input/customSR --input_name 11.png --noisy_input_name 24_input.png --sr_factor 2 --ker_size 2 --niter 1000  --lr_g 0.001 --lr_d 0.001 --custom_sr_alpha 20 --frozenWeight 0.7 --nc_im 1 --nc_z 1 --skip_training 1 --threshold 128 
# git add .
# git commit -m "run5"