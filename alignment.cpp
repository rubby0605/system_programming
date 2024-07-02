#include <iostream>
#include <opencv2/opencv.hpp>
#include <opencv2/features2d.hpp>
#include <opencv2/highgui.hpp>
#include <opencv2/imgproc.hpp>

using namespace cv;
using namespace std;

int main() {
    // 讀取參考圖像
    string refFilename = "Quarter_A.png";
    cout << "Reading reference image : " << refFilename << endl;
    Mat im1 = imread(refFilename, IMREAD_COLOR);
    cvtColor(im1, im1, COLOR_BGR2RGB);

    // 讀取待對齊圖像
    string imFilename = "Quarter_NA4.png";
    cout << "Reading image to align : " << imFilename << endl;
    Mat im2 = imread(imFilename, IMREAD_COLOR);
    cvtColor(im2, im2, COLOR_BGR2RGB);

    // 顯示原圖像和待對齊圖像
    namedWindow("Original Form", WINDOW_NORMAL);
    imshow("Original Form", im1);
    namedWindow("Scanned Form", WINDOW_NORMAL);
    imshow("Scanned Form", im2);
    waitKey(0);

    // 轉換為灰度圖像
    Mat im1Gray, im2Gray;
    cvtColor(im1, im1Gray, COLOR_BGR2GRAY);
    cvtColor(im2, im2Gray, COLOR_BGR2GRAY);

    // 檢測 ORB 特徵並計算描述符
    int MAX_NUM_FEATURES = 500;
    Ptr<ORB> orb = ORB::create(MAX_NUM_FEATURES);
    vector<KeyPoint> keypoints1, keypoints2;
    Mat descriptors1, descriptors2;
    orb->detectAndCompute(im1Gray, noArray(), keypoints1, descriptors1);
    orb->detectAndCompute(im2Gray, noArray(), keypoints2, descriptors2);

    // 顯示檢測到的特徵點
    Mat im1_display, im2_display;
    drawKeypoints(im1, keypoints1, im1_display, Scalar(255, 0, 0), DrawMatchesFlags::DRAW_RICH_KEYPOINTS);
    drawKeypoints(im2, keypoints2, im2_display, Scalar(255, 0, 0), DrawMatchesFlags::DRAW_RICH_KEYPOINTS);

    namedWindow("Keypoints in Original Form", WINDOW_NORMAL);
    imshow("Keypoints in Original Form", im1_display);
    namedWindow("Keypoints in Scanned Form", WINDOW_NORMAL);
    imshow("Keypoints in Scanned Form", im2_display);
    waitKey(0);

    // 匹配描述符
    Ptr<DescriptorMatcher> matcher = DescriptorMatcher::create(DescriptorMatcher::BRUTEFORCE_HAMMING);
    vector<DMatch> matches;
    matcher->match(descriptors1, descriptors2, matches);

    // 按得分排序
    sort(matches.begin(), matches.end(), [](const DMatch &a, const DMatch &b) {
        return a.distance < b.distance;
    });

    // 保留好的匹配
    int numGoodMatches = matches.size() * 0.10;
    matches.erase(matches.begin() + numGoodMatches, matches.end());

    // 繪製匹配點
    Mat im_matches;
    drawMatches(im1, keypoints1, im2, keypoints2, matches, im_matches);

    namedWindow("Matches", WINDOW_NORMAL);
    imshow("Matches", im_matches);
    waitKey(0);

    // 提取匹配點的位置
    vector<Point2f> points1(matches.size());
    vector<Point2f> points2(matches.size());
    for (size_t i = 0; i < matches.size(); i++) {
        points1[i] = keypoints1[matches[i].queryIdx].pt;
        points2[i] = keypoints2[matches[i].trainIdx].pt;
    }

    // 計算單應性矩陣
    Mat h = findHomography(points2, points1, RANSAC);

    // 使用單應性矩陣進行透視變換
    Mat im2_reg;
    warpPerspective(im2, im2_reg, h, im1.size());

    // 顯示對齊結果
    namedWindow("Aligned Scanned Form", WINDOW_NORMAL);
    imshow("Aligned Scanned Form", im2_reg);
    waitKey(0);

    return 0;
}
