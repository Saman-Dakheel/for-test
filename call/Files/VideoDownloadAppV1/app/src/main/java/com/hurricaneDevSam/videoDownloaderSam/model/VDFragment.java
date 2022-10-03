/*
 * Copyright (c) 2021.  Hurricane Development Studios
 */

package com.hurricaneDevSam.videoDownloaderSam.model;

import androidx.fragment.app.Fragment;

import com.hurricaneDevSam.videoDownloaderSam.VDApp;
import com.hurricaneDevSam.videoDownloaderSam.activity.MainActivity;

public class VDFragment extends Fragment {

    public MainActivity getVDActivity() {
        return (MainActivity) getActivity();
    }

    public VDApp getVDApp() {
        return (VDApp) getActivity().getApplication();
    }
}
