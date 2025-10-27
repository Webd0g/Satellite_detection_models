from ultralytics import YOLO

model = YOLO(r"C:\Users\riley\OneDrive\Documents\University\Year_3\Semester_2\Applied_science_project_2\machine_learning_detection_approach\Trained_models\Final_models\Satellite_streaks_detection_model_14_Sept_2025\weights\best.pt")
# Test on a single image
results = model.predict(r"C:\Users\riley\OneDrive\Documents\University\Year_3\Semester_2\Applied_science_project_2\Image_data\Streak_like_training_images\September_04_and_05_pngs\00076647_Az_336_Elev_43_5.000secs_Light.png", save=True)

# Test on a folder of images/
results = model.predict(source= r"C:\Users\riley\OneDrive\Documents\University\Year_3\Semester_2\Applied_science_project_2\Image_data\Streak_like_testing_images\png_images",save_txt=True, imgsz = 1280, conf = 0.25, save = True, name = '4th_sept_streaks_model_evaluation_results', project = r"C:\Users\riley\OneDrive\Documents\University\Year_3\Semester_2\Applied_science_project_2\machine_learning_detection_approach\final_model_evaluation")

# Run predictions on holdout test set
results = model.predict(
    source=r"C:\Users\riley\OneDrive\Documents\University\Year_3\Semester_2\Applied_science_project_2\Image_data\Streak_like_testing_images\png_images",
    save=True, save_conf=True, conf=0.25)

# By default, images with detections are saved in runs/predict/exp
print("Gallery saved in:", results[0].save_dir)

validation_results = model.val(dataset =r"C:\Users\riley\OneDrive\Documents\University\Year_3\Semester_2\Applied_science_project_2\machine_learning_detection_approach\Testing_data\data.yaml", imgsz = 1280, conf = .25, )