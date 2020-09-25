import { ComponentFixture, TestBed } from '@angular/core/testing';

import { HubViewerComponent } from './hub-viewer.component';

describe('HubViewerComponent', () => {
  let component: HubViewerComponent;
  let fixture: ComponentFixture<HubViewerComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ HubViewerComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(HubViewerComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
