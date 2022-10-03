/*
 * Copyright (c) 2021.  Hurricane Development Studios
 */

package com.hurricaneDevSam.videoDownloaderSam.download;

//interface created outside DownloadsInactive in a different file to avoid cyclic inheritance
public interface OnDownloadWithNewLinkListener {
    void onDownloadWithNewLink(DownloadVideo download);
}
