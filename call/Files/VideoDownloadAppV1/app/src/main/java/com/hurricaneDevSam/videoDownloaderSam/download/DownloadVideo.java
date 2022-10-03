/*
 * Copyright (c) 2021.  Hurricane Development Studios
 */

package com.hurricaneDevSam.videoDownloaderSam.download;

import java.io.Serializable;

public class DownloadVideo implements Serializable {
    public String size;
    public String type;
    public String link;
    public String name;
    public String page;
    public String website;
    public boolean chunked;
}
