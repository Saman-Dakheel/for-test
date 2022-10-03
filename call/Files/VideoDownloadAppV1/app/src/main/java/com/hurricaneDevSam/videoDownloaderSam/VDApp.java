/*
 * Copyright (c) 2021.  Hurricane Development Studios
 */

package com.hurricaneDevSam.videoDownloaderSam;

import android.app.Application;
import android.content.Intent;

import com.google.android.gms.ads.MobileAds;
import com.hurricaneDevSam.videoDownloaderSam.activity.MainActivity;
import com.hurricaneDevSam.videoDownloaderSam.download.DownloadManager;

public class VDApp extends Application {
    private static VDApp instance;
    private Intent downloadService;
    private MainActivity.OnBackPressedListener onBackPressedListener;

    @Override
    public void onCreate() {
        super.onCreate();
        instance = this;
        MobileAds.initialize(this);
        downloadService = new Intent(getApplicationContext(), DownloadManager.class);
    }

    public Intent getDownloadService() {
        return downloadService;
    }

    public static VDApp getInstance() {
        return instance;
    }

    public MainActivity.OnBackPressedListener getOnBackPressedListener() {
        return onBackPressedListener;
    }

    public void setOnBackPressedListener(MainActivity.OnBackPressedListener onBackPressedListener) {
        this.onBackPressedListener = onBackPressedListener;
    }
}
