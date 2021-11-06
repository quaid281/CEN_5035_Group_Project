import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ClassificationEditorComponent } from './classification-editor.component';

describe('ClassificationEditorComponent', () => {
  let component: ClassificationEditorComponent;
  let fixture: ComponentFixture<ClassificationEditorComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ClassificationEditorComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ClassificationEditorComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
